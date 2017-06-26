import getpass
import logging
import random
import re
import shlex

import paramiko
from ldap3 import Server, Connection
from passlib.hash import sha512_crypt

from iselab.models import User
from iselab.settings import LDAP_SERVER, QUERY_STRING, PRIVKEY, KALI_HOSTS

logger = logging.getLogger('iasg')

TERMS = "TERMS AND CONDITIONS: While ISELab is a safe environment for hacking, your activities and usage must remain " \
        "in compliance with all applicable local, state, and federal laws, as well as university policy. Notably, " \
        "you may not use " \
        "this system to attack ISU infrastructure or others outside the environment. IASG will not be held liable for " \
        "any damages, " \
        "whether physical, virtual, imaginary, stress-related, or otherwise, that may arise from the use of these " \
        "systems. " \
        "Usage of this system may be logged and monitored for abuse. With all that in mind, it is most important that " \
        "you have fun!\n\n" \
        "By typing 'yes' below, you affirm that you have read and understood the terms and conditions."


def provision(user: User):
    with paramiko.SSHClient() as ssh:
        try:
            key = paramiko.RSAKey.from_private_key_file(PRIVKEY)
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(user.host, username='provisioner', pkey=key)
            ssh.exec_command("sudo useradd {} -s /bin/bash".format(shlex.quote(user.netid)))
            ssh.exec_command("echo '{}:{}' | sudo chpasswd ".format(shlex.quote(user.netid), user.privpass))
            ssh.exec_command("sudo mkdir /home/{}".format(shlex.quote(user.netid)))
            ssh.exec_command("sudo chown -R {0}:{0} /home/{0}".format(shlex.quote(user.netid)))
        except Exception as e:
            logger.error("Error provisioning {}: {}".format(user.netid, e))
            print("Warning!!! We couldn't fully set up your account. Get help in #iselab on https://iasg.slack.com.")
        else:
            logger.info("Provisioned {} on {}".format(user.netid, user.host))


def validate_uid(username: str) -> str:
    return re.sub(r'[^\d\w]', '', username)


def check_netid(username: str) -> str:
    server = Server(LDAP_SERVER)
    conn = Connection(server, auto_bind=True)
    conn.search(QUERY_STRING, '(uid={})'.format(validate_uid(username)), attributes=['cn'])
    user = None
    try:
        user = conn.entries[0].cn[0]
    except TypeError:
        logger.warning("NetID {} response was: {}".format(username, conn.entries))
    finally:
        conn.unbind()
    return user


def create_user(username: str) -> User:
    print("It looks like it's your first time using IASG ISELab!")
    print()
    name = check_netid(username)
    if not name:
        return None
    print(TERMS)
    if not input("Accept [yes/no]? ").lower() == 'yes':
        print("Bye.")
        raise SystemExit
    print("Welcome,", name + "!")
    print("Now, create a strong password. Do not reuse an existing password!")
    print()
    while True:
        password = getpass.getpass()
        confirm_password = getpass.getpass("Confirm Password: ")
        if password == confirm_password:
            try:
                user = User.create(netid=username, password=sha512_crypt.hash(password),
                            host='kali{}.iasg.net'.format(random.randint(1, KALI_HOSTS)))
            except Exception as e:
                logger.error("Error creating account {}: {}".format(username, e))
                print("Error! Couldn't create your account. Please request help in #iselab on https://iasg.slack.com.")
                raise SystemExit
            logger.info("Created account {}".format(username))
            print("Setting up your account. Please wait...")
            provision(user)
            return user
        else:
            print("Passwords didn't match! Try again.")

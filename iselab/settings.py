from peewee import SqliteDatabase

KALI_HOSTS = 1
LDAP_SERVER = 'ldap://ldap.iastate.edu'
QUERY_STRING = 'ou=people,dc=iastate,dc=edu'
PRIVKEY = '/home/iasg/.ssh/id_rsa'
db = SqliteDatabase('iasg.db')
EMAIL_FROM = 'iasg-cabinet@iastate.edu'
SMTP_SERVER = None
SMTP_PORT = 25
SMTP_USERNAME = ''
SMTP_PASSWORD = ''
VPN_CONFIG = None
DEBUG = False
SECRET_KEY = None
WETTY = ''

try:
    from iselab.settings_local import *
except ImportError:
    pass

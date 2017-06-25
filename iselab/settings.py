from peewee import SqliteDatabase

KALI_HOSTS = 1
LDAP_SERVER = 'ldap://ldap.iastate.edu'
QUERY_STRING = 'ou=people,dc=iastate,dc=edu'
PRIVKEY = '/home/iasg/.ssh/id_rsa'
db = SqliteDatabase('iasg.db')
try:
    from settings_local import *
except ImportError:
    pass

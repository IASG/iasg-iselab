KALI_HOSTS = 1
LDAP_SERVER = 'ldap://ldap.iastate.edu'
QUERY_STRING = 'ou=people,dc=iastate,dc=edu'
PRIVKEY = '/home/iasg/.ssh/id_rsa'
try:
    from settings_local import *
except ImportError:
    pass

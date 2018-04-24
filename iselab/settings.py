from peewee import SqliteDatabase

# Database to store user accounts
db = SqliteDatabase('iasg.db')
# db = MySQLDatabase(database='iselab', host='localhost', user='iselab', password='iselab') # for a MySQL Database

# The from address for account creation emails
EMAIL_FROM = 'iasg-cabinet@iastate.edu'

# SMTP Server configuration
SMTP_SERVER = None
SMTP_PORT = 25
SMTP_USERNAME = ''
SMTP_PASSWORD = ''

# Path to a VPN config, will be made available for download
VPN_CONFIG = None

# Enable the Werkzeug debugger. Do not use in production!
DEBUG = False

# The key to use for secure session generation.
# Set to something long and random
SECRET_KEY = None

# Used by the hacky browser-in-browser. Set to any proxy server
# in the internal environment as per
# http://docs.python-requests.org/en/master/user/advanced/#proxies
PROXIES = {'http': 'http://199.100.16.100:3128'}

# Public-facing URL to use for the application,
# e.g. https://iasg.iac.iastate.edu/iselab
URL = 'http://localhost/'

# Host to display for the SSH hop
HOST = ''

try:
    from iselab.settings_local import *
except ImportError:
    pass

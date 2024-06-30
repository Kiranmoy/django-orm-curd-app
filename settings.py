import sys
import oracledb
oracledb.version="19"
sys.modules["cx_Oracle"]=oracledb

# Oracle 19c DB
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.oracle',
        'NAME': 'orclpractice',
        'USER': 'System',
        'PASSWORD': 'Oracle123',
        'HOST': 'localhost',
        'PORT': '1521',
    }
}

INSTALLED_APPS = (
    'crud',
)

SECRET_KEY = 'SECRET KEY for this Django Project'

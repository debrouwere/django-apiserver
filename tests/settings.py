import os

ADMINS = (
    ('test@example.com', 'Mr. Test'),
)

BASE_PATH = os.path.abspath(os.path.dirname(__file__))

MEDIA_ROOT = os.path.normpath(os.path.join(BASE_PATH, 'media'))

DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = 'apiserver.db'
TEST_DATABASE_NAME = 'apiserver-test.db'

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'apiserver',
]

DEBUG = True
TEMPLATE_DEBUG = DEBUG
CACHE_BACKEND = 'locmem://'

# coding=utf-8
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = 'dsez8g^+7v-vyg&j!1j=0buon^n@*!4quieq8m0ui@p)cqb5bh'

DEBUG = True
TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['localhost']
INTERNAL_IPS = ['127.0.0.1']

ROOT_URLCONF = 'citydefects.urls'

WSGI_APPLICATION = 'citydefects.wsgi.application'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'easy_thumbnails',

    'citydefects',
    'defect',
]

MIDDLEWARE_CLASSES = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

TEMPLATE_CONTEXT_PROCESSORS = [
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
    'comment.context_processors.facebook'
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

DEFAULT_LAT = '50.827978'
DEFAULT_LNG = '15.525992'

GOOGLE_GEOCODE_URL = (u'http://maps.googleapis.com/maps/api/geocode/json?'
                      u'sensor=false&address=%(address)s&'
                      u'components=locality:Szklarska Poręba|country:Poland')

THUMBNAIL_ALIASES = {
    '': {
        'small': {'size': (250, 250)},
        'big': {'size': (1024, )},
    },
}

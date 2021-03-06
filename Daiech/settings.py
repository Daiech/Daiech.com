"""
Django settings for Daiech project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from django.conf import global_settings
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ia7rrg2xmrtrt#dh*zm5ea(b%1fsfghdgnaxa0zhiu(gf^r$u4'

# SECURITY WARNING: don't run with debug turned on in production!
try:
    from .local_settings import DEBUG
except ImportError:
    DEBUG = True

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = [".daiech.com", ".daiech.com.", "localhost"]


# Application definition

APPS = ["apps.website", "apps.github", "apps.ads"]

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rosetta',
) + tuple(APPS)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'Daiech.urls'

WSGI_APPLICATION = 'Daiech.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

try:
    from .local_settings import DATABASES
except ImportError:
    DATABASES = {'default': {'ENGINE': 'django.db.backends.sqlite3','NAME': os.path.join(BASE_DIR, 'db.sqlite3'),}}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'America/Bogota'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOGIN_URL = "/admin"

LOCALE_PATHS = tuple([os.sep.join([BASE_DIR,APP.replace('.',os.sep),'locale']) for APP in APPS])

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

try:
    from local_settings import STATIC_ROOT
except ImportError:
    STATIC_ROOT = ""

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR , 'public/static').replace('\\','/'),
)


TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates').replace('\\', '/')
)


TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    'django.core.context_processors.request',
    'apps.website.context_processors.is_debug',
)

ugettext = lambda s: s
LANGUAGES = (
    ('es', ugettext('Spanish')),
    ('en', ugettext('English')),
)

MIDDLEWARE_CLASSES = global_settings.MIDDLEWARE_CLASSES + (
    'django.middleware.locale.LocaleMiddleware',
)
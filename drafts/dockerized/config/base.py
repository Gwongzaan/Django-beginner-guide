import os.path
from pathlib import Path

from django.conf.global_settings import LOGIN_URL

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY',
                            "django-insecure-caebb+zs_ai6pc5g-kb&jlt626l4sgi*fjwhn5k8+9)vlznx+mg9ubl")
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG') == 'True'

ALLOWED_HOSTS = ["127.0.0.1:8000", '0.0.0.0:8000', 'localhost']
CORS_ORIGIN_ALLOW_ALL = os.environ.get('CORS_ORIGIN_ALLOW_ALL') == 'True'
CORS_ORIGIN_WHITELIST = []
CSRF_TRUSTED_ORIGINS = []

if DEBUG:
    if os.environ.get("ALLOWED_HOSTS", False):
        try:
            ALLOWED_HOSTS += os.environ.get("ALLOWED_HOSTS").split(',')
        except Exception as e:
            print("Cant set ALLOWED_HOSTS, using default instead")

    if os.environ.get('CORS_ORIGIN_WHITELIST', False):
        try:
            CORS_ORIGIN_WHITELIST += os.environ.get('CORS_ORIGIN_WHITELIST').split(',')
        except Exception as e:
            print('Cant set CORS_ORIGIN_WHITELIST, using default instead')

    if os.environ.get('CSRF_TRUSTED_ORIGINS', False) :
        try:
            CSRF_TRUSTED_ORIGINS += os.environ.get('CSRF_TRUSTED_ORIGINS').split(',')
        except Exception as e:
            print('Cant set CSRF_TRUSTED_ORIGINS, using the default instead')

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}


# DATAbase SETTINGS
# default database is sqlite3
DATABASES = {
    'default':{
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
}

if os.getenv('MULTI_DB') == 'True':
    DATABASES = {
        'default': {},
        'sqlite':{},
        'postgresql':{},
    }
if os.getenv('DJANGO_DB') == 'postgres':
    DATABASES = {
       'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.getenv('POSTGRES_DB', 'postgres'),
            'USER': os.getenv('POSTGRES_USER', 'postgres'),
            'PASSWORD': os.getenv('POSTGRES_PASSWORD', 'postgres'),
            'HOST': os.getenv('POSTGRES_HOST', 'localhost'),
            'PORT': os.getenv('POSTGRES_POST', '5432'),
        }
    }

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
#################################################################
#           Third party INSTALLED_APPS
#################################################################
INSTALLED_APPS += [
    # 'corsheaders',
]

if DEBUG:
    INSTALLED_APPS += [
        'rest_framework',
    ]

#################################################################
#           customized INSTALLED_APPS
#################################################################
INSTALLED_APPS += [
    'blog',
    'account',
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
#################################################################
#          THIRD PARTY MIDDLEWARE
#################################################################
MIDDLEWARE += [
    'corsheaders.middleware.CorsMiddleware',
]

#################################################################
#           CUSTOMIZED MIDDLEWARE
#################################################################
MIDDLEWARE += []

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'project.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

AUTH_USER_MODEL = 'auth.User'

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'
# TIME_ZONE = 'UTC'
USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [
    # os.path.join(BASE_DIR, 'staticfiles'),
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_URL = '/account/login/'
LOGIN_REDIRECT_URL = '/home/'

# Celery Configuration
CELERY_BROKER_URL = 'redis://redis:6379/0'
CELERY_RESULT_BACKEND = 'redis://redis:6379/0'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'UTC'

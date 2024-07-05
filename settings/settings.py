"""
Django settings for settings project.

Generated by 'django-admin startproject' using Django 5.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-9l_%ojsx%hw(eio&m_zg#aby_lazy7_*np$)%+=(vmm!z2#^%7'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# DEBUG = True

ALLOWED_HOSTS = ['*']
CORS_ALLOWED_ORIGINS = [
    'https://test.askgroup.az',
    'https://askgroup.az',
    'https://www.askgroup.az',
]
# Application definition
CSRF_TRUSTED_ORIGINS = [
    'https://test.askgroup.az',
    'http://test.askgroup.az',
    'https://www.askgroup.az',
    'https://askgroup.az',
    'http://www.askgroup.az',
    'http://askgroup.az',
]


INSTALLED_APPS = [
    'modeltranslation',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    #third party apps
    'marketapp',
    'ckeditor',
    'ckeditor_uploader',
    'rosetta', 
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'language.DefaultLanguageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
]

ROOT_URLCONF = 'settings.urls'
import os
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
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

WSGI_APPLICATION = 'settings.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

from django.utils.translation import gettext_lazy as _



LANGUAGES = [
    ('az', _('Az')),
    ('en', _('En')),
    ('ru', _('Ru')),
]

PARLER_LANGUAGES = {
    None : (
        {'code': 'az',},
        {'code': 'en',},
        {'code': 'ru',},
    ),
    'default': {
        'fallbacks': [],
        'hide_untranslated': False,
    }
}

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]

LANGUAGE_CODE = 'az'
MODELTRANSLATION_DEFAULT_LANGUAGE = 'az'
DEFAULT_LANGUAGE = 'az'


TIME_ZONE = 'Asia/Baku'
SITE_ID = 1
USE_I18N = True
USE_TZ = True


STATIC_URL = '/static/'
if DEBUG:
    STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
else:
    STATIC_ROOT = os.path.join(BASE_DIR, "static")

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')


CKEDITOR_BASEPATH = '/static/ckeditor/ckeditor/'
CKEDITOR_UPLOAD_PATH = 'uploads'


SILENCED_SYSTEM_CHECKS = ['ckeditor.W001']
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': None,
        'extraPlugins': 'blockquote',
        "versionCheck": False
    },
}
DATA_UPLOAD_MAX_MEMORY_SIZE = 12428800
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')

TRANSLATABLE_MODEL_MODULES = ["marketapp.models", ]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

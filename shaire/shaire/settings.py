"""
Django settings for shaire project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'qa#rce049r5hc7$$yl*u0(+x25pkwro%r3an5%^bvco#sw=m!8'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'loginsys',
    'user_profile',
    'alerts',
    'captcha',
    'search',
    'chat',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'shaire.urls'

WSGI_APPLICATION = 'shaire.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
    os.path.join(BASE_DIR, 'loginsys/templates'),
    os.path.join(BASE_DIR, 'user_profile/templates'),
    os.path.join(BASE_DIR, 'alerts/templates'),
    os.path.join(BASE_DIR, 'search/templates'),
    os.path.join(BASE_DIR, 'chat/templates'),
    # '/home/nikit0s/djangoproject/bin/shaire/templates',
    # '/home/nikit0s/djangoproject/bin/shaire/loginsys/templates',
    # '/home/nikit0s/djangoproject/bin/shaire/user_profile/templates',
    # '/home/nikit0s/djangoproject/bin/shaire/alerts/templates',
    # '/home/nikit0s/djangoproject/bin/shaire/search/templates',
    # '/home/nikit0s/djangoproject/bin/shaire/chat/templates',
)

STATICFILES_DIRS = (
    ('static', os.path.join(BASE_DIR, 'static')),
)

#AUTH_USER_MODEL = 'loginsys.Users'

EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025

ADMINS = (
    ('Nikita', 'grizzlyarchi@gmail.com'),
    ('Fedor', 'kakoi_to_email@gmail.com')
)

RECAPTCHA_PUBLIC_KEY = '6LeT5_oSAAAAADlevx65QaGQSytkeA8z5zbf9GSZ'
RECAPTCHA_PRIVATE_KEY = '6LeT5_oSAAAAAC9p_ncoAGMJ0zcFAzN9Uh7UUEVp'
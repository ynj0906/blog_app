"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 2.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
#localsettings.pyに移動

#環境変数を別ファイルに分けるために追加
from socket import gethostname
from os import environ
HOSTNAME = gethostname()

if 'DESKTOP' in HOSTNAME:
    from . import local_settings
    SECRET_KEY = local_settings.SECRET_KEY#以下Djangoシークレットキーの設定
    NAME = local_settings.NAME#以下MySqlの設定
    USER = local_settings.USER
    PASSWORD = local_settings.PASSWORD
    HOST = local_settings.HOST
    # DEBUG = True
else:
    SECRET_KEY = environ['Django_SECRET_KEY']
    DEBUG = False

# SECURITY WARNING: don't run with debug turned on in production!
"""DEBUGの設定は移動"""
DEBUG = True


ALLOWED_HOSTS = ["*"]#追加、本来は許可するホストを指定スべき

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'contents.apps.ContentsConfig',#追加
    'django.forms',
    'markdownx',

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

ROOT_URLCONF = 'config.urls'

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
                'contents.context_processors.common',#追加
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': NAME,#移動
        'USER': USER,#移動
        'PASSWORD': PASSWORD,#移動
        'HOST': HOST,#移動
        'PORT': '3306',
        'ATOMIC_REQUESTS': True,
        'OPTIONS': {
            'charset': 'utf8mb4',
            'sql_mode': 'TRADITIONAL,NO_AUTO_VALUE_ON_ZERO',

        }
    }
}
#
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/


#css/js/画像の配信用に追加
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

#ログイン/ログアウト時のリダイレクト用に追加
LOGIN_REDIRECT_URL = "/contents/main"
LOGOUT_REDIRECT_URL = "/contents/main"

#画像のアップロード用に追加
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

#追加
# if DEBUG:
#     def show_toolbar(request):
#         return True
# INSTALLED_APPS += (
#     'debug_toolbar',
# )
# MIDDLEWARE += (
#     'debug_toolbar.middleware.DebugToolbarMiddleware',)
# DEBUG_TOOLBAR_CONFIG = {
#     'SHOW_TOOLBAR_CALLBACK': show_toolbar,
# }

FORM_RENDERER = 'django.forms.renderers.TemplatesSetting'

MARKDOWNX_MARKDOWN_EXTENSIONS = [
    'markdown.extensions.extra',
    'markdown.extensions.toc',
]
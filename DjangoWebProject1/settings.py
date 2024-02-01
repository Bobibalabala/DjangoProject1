"""
Django settings for DjangoWebProject1 project.

Based on 'django-admin startproject' using Django 2.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

from logging.handlers import DEFAULT_HTTP_LOGGING_PORT
import os
import posixpath
import sys 


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '9854a864-a24d-4e73-bd16-02d9f42acf19'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# LOGIN_REDIRECT_URL = '/home'  # ��½��֤�ɹ�֮���ض����ҳ��
# LOGOUT_REDIRECT_URL = '/login'  # ��½ʧ�ܵ���Ҫ�ض����ҳ��

# Application references
# https://docs.djangoproject.com/en/2.1/ref/settings/#std:setting-INSTALLED_APPS
# �������µ�app��ʱ����Ҫ���������app����Ϣ
INSTALLED_APPS = [
    'app',
    # Add your apps here to enable them
    'django.contrib.admin',  #  ����django��һЩ����
    'django.contrib.auth',  # ����django���û���֤
    'django.contrib.contenttypes',  # ������ģ�͵��������ͽ��й���Ͳ����Ĺ���
    'django.contrib.sessions',  # �ṩ�Ự�����ܹ�����
    'django.contrib.messages',  # �ṩ��Ϣ���ݵĹ���
    'django.contrib.staticfiles',  # ���ڴ���̬�ļ����ͻ���
]

# Middleware framework
# https://docs.djangoproject.com/en/2.1/topics/http/middleware/

# middleware��һ����ܼ���Ĳ��ϵͳ����������Ա���������Ӧ��������и�Ԥ�����ƴ����߼����м������django�����������λ����ͼ��
# ���֮���һϵ�й��Ӻ����������������󵽴���ͼ֮ǰ���뿪��ͼ֮��ִ���Զ�����߼�
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ��·���ļ�
ROOT_URLCONF = 'DjangoWebProject1.urls'

# Template configuration
# https://docs.djangoproject.com/en/2.1/topics/templates/
# ģ������
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'DjangoWebProject1.wsgi.application'
# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators
# ����Ϸ�����֤����
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
# https://docs.djangoproject.com/en/2.1/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/
# ��̬�ļ���Ŀ¼
STATIC_URL = '/static/'
STATIC_ROOT = posixpath.join(*(BASE_DIR.split(os.path.sep) + ['static']))

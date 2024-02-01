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


# LOGIN_REDIRECT_URL = '/home'  # 登陆验证成功之后重定向的页面
# LOGOUT_REDIRECT_URL = '/login'  # 登陆失败等需要重定向的页面

# Application references
# https://docs.djangoproject.com/en/2.1/ref/settings/#std:setting-INSTALLED_APPS
# 当创建新的app的时候需要在这里添加app的信息
INSTALLED_APPS = [
    'app',
    # Add your apps here to enable them
    'django.contrib.admin',  #  用于django的一些管理
    'django.contrib.auth',  # 用于django的用户认证
    'django.contrib.contenttypes',  # 对数据模型的内容类型进行管理和操作的功能
    'django.contrib.sessions',  # 提供会话管理功能管理功能
    'django.contrib.messages',  # 提供消息传递的功能
    'django.contrib.staticfiles',  # 用于处理静态文件给客户端
]

# Middleware framework
# https://docs.djangoproject.com/en/2.1/topics/http/middleware/

# middleware是一个框架级别的插件系统，允许开发人员在请求和响应处理过程中干预并定制处理逻辑，中间件是在django请求处理过程中位于视图和
# 框架之间的一系列钩子函数，允许你在请求到达视图之前或离开视图之后执行自定义的逻辑
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# 根路由文件
ROOT_URLCONF = 'DjangoWebProject1.urls'

# Template configuration
# https://docs.djangoproject.com/en/2.1/topics/templates/
# 模板配置
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
# 密码合法性验证配置
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
# 静态文件的目录
STATIC_URL = '/static/'
STATIC_ROOT = posixpath.join(*(BASE_DIR.split(os.path.sep) + ['static']))

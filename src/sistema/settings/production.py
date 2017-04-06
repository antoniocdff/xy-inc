# -*- coding: utf-8 -*-
import os
from .base import *

DEBUG = False
TEMPLATE_DEBUG = False
ALLOWED_HOSTS = ["xyinc.antoniocarlosdias.com.br", ]

REST_FRAMEWORK["DEFAULT_RENDERER_CLASSES"] = ('rest_framework.renderers.JSONRenderer',)


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, "templates"),
            os.path.join(BASE_DIR, '..', '..', '..', 'sistema', 'src'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages'
            ],
        },
    },
]


SECRET_KEY = "1qa2ws3ed!QA@WS#ED"


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'tootico_xyinc',
        'USER': 'xyinc',
        'PASSWORD': '1qa2ws3ed!QA@WS#ED',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
CSRF_COOKIE_DOMAIN = '.antoniocarlosdias.com.br'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
        },
        'addresses': {
            'handlers': ['console'],
            'level': 'ERROR'
        }
    },
}

# -*- coding: utf-8 -*-
from .base import *

DEBUG = True
SECRET_KEY = 'local'

ALLOWED_HOSTS = []

INSTALLED_APPS += ('debug_toolbar',
                   'django_extensions', )
MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware', )

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': "xyinc",
        'USER': "postgres",
        'PASSWORD': "postgres",
        'HOST': "localhost",
        'PORT': '5432',
    }
}

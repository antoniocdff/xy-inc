# coding: utf-8
import os
import sys
from django.core.wsgi import get_wsgi_application
sys.path.append('/home/tootico/xyinc/sistema/src')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sistema.settings.production")
application = get_wsgi_application()

# -*- coding: utf-8 -*-
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from .views import home

router = DefaultRouter(trailing_slash=False)

schema_view = get_swagger_view(title='XY INC')

urlpatterns = [
    url(r'^api/token/$', obtain_auth_token, name='api-token'),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r"^$", home, name='home'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

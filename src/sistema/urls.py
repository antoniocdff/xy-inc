# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view

from sistema import views
from sistema import viewsets

router = DefaultRouter(trailing_slash=False)

schema_view = get_swagger_view(title='XY INC')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/token/$', obtain_auth_token, name='api-token'),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^modelos/$', views.listar_modelos, name='listar_modelos'),
    url(r'^modelos/criar/$', views.criar_modelo, name='criar_modelo'),
    url(r'^modelos/(?P<pk>\d+)/editar/$', views.editar_modelo, name='editar_modelo'),
    url(r'^modelos/(?P<pk>\d+)/excluir/$', views.excluir_modelo, name='excluir_modelo'),

    url(r'^modelos/(?P<modelo_pk>\d+)/campos/$', views.listar_campos, name='listar_campos'),
    url(r'^modelos/(?P<modelo_pk>\d+)/campos/criar/$', views.criar_campo, name='criar_campo'),
    url(r'^modelos/(?P<modelo_pk>\d+)/campos/(?P<campo_pk>\d+)/editar/$', views.editar_campo, name='editar_campo'),
    url(r'^modelos/(?P<modelo_pk>\d+)/campos/(?P<pk>\d+)/excluir/$', views.excluir_campo, name='excluir_campo'),

    # url(r'^tables/$', views.list_tables, name='table_list'),
    # url(r'^tables/create/$', views.create_table, name='table_create'),
    # url(r'^tables/(?P<pk>\d+)/update/$', views.update_table, name='table_update'),
    # url(r'^tables/(?P<pk>\d+)/delete/$', views.delete_table, name='table_delete'),

    # url(r'^tables/(?P<table_pk>\d+)/fields/$', views.list_fields, name='field_list'),
    # url(r'^tables/(?P<table_pk>\d+)/fields/create/$', views.create_field, name='field_create'),
    # url(r'^tables/(?P<table_pk>\d+)/fields/(?P<field_pk>\d+)/update/$', views.update_field, name='field_update'),
    # url(r'^tables/(?P<table_pk>\d+)/fields/(?P<pk>\d+)/delete/$', views.delete_field, name='field_delete'),

    url(r'^api/(?P<model>\w+)/', viewsets.GeneralViewSet.as_view({'get': 'list'}))

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

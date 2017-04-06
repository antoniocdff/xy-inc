# -*- coding: utf-8 -*-
from django.template import Template, TemplateDoesNotExist, loader
from rest_framework import compat
from django_filters.rest_framework import backends


class TempBackend(backends.DjangoFilterBackend):

    def to_html(self, request, queryset, view):
        filter_class = self.get_filter_class(view, queryset)
        if not filter_class:
            return None
        filter_instance = filter_class(request.query_params, queryset=queryset)

        filter_instance.form

        try:
            template = loader.get_template(self.template)
        except TemplateDoesNotExist:
            template = Template(backends.template_default)

        return compat.template_render(template,
                                      context={'filter': filter_instance})

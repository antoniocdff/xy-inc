# -*- coding: utf-8 -*-
from rest_framework import viewsets

from sistema.serializers import GeneralSerializer


class GeneralViewSet(viewsets.ModelViewSet):

    def get_queryset(self):
        import pdb; pdb.set_trace()
        model = self.kwargs.get('model')
        return model.objects.all()

    def get_serializer_class(self):
        GeneralSerializer.Meta.model = self.kwargs.get('model')
        return GeneralSerializer

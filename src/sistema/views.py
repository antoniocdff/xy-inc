# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from mutant import models

from sistema.forms import AddFieldForm, get_field_def_form
from sistema.utils import get_mutant_type


class ModeloListaView(ListView):
    model = models.ModelDefinition
    context_object_name = 'table_list'
    template_name = 'sistema/table_list.html'


listar_modelos = ModeloListaView.as_view()


class ModeloCriaView(CreateView):
    model = models.ModelDefinition
    template_name = 'sistema/table_save.html'
    success_url = reverse_lazy('listar_modelos')


criar_modelo = ModeloCriaView.as_view()


class ModeloEditaView(UpdateView):
    model = models.ModelDefinition
    template_name = 'sistema/table_save.html'
    success_url = reverse_lazy('listar_modelos')


editar_modelo = ModeloEditaView.as_view()


class ModeloExcluiView(DeleteView):
    model = models.ModelDefinition
    template_name = 'sistema/table_delete.html'
    success_url = reverse_lazy('listar_modelos')


excluir_modelo = ModeloExcluiView.as_view()


class CampoListaView(ListView):
    model = models.FieldDefinition
    context_object_name = 'field_list'
    template_name = 'sistema/field_list.html'

    def get_queryset(self):
        modelo_pk = self.kwargs.get('modelo_pk', None)
        return self.model.objects.filter(model_def_id=modelo_pk)

    def get_context_data(self, **kwargs):
        context = super(CampoListaView, self).get_context_data(**kwargs)
        modelo_pk = self.kwargs.get('modelo_pk', None)
        try:
            parent_table = models.ModelDefinition.objects.get(pk=modelo_pk)
        except models.ModelDefinition.DoesNotExist:
            pass
        else:
            context['parent_table_name'] = parent_table.name

        context['parent_table_id'] = modelo_pk
        context['field_type_form'] = AddFieldForm()

        return context


listar_campos = CampoListaView.as_view()


class SuccessUrlMixin(object):

    def get_reversed_success_url(self):
        try:
            modelo_pk = self.kwargs['modelo_pk']
        except KeyError:
            return reverse('listar_modelos')
        else:
            return reverse('listar_campos', kwargs={'modelo_pk': modelo_pk})


class CampoCriaView(SuccessUrlMixin, CreateView):
    template_name = 'sistema/field_save.html'

    def get_success_url(self):
        self.success_url = self.get_reversed_success_url()
        return super(CampoCriaView, self).get_success_url()

    def _prepare_dynamic_form(self, request, modelo_pk, super_func):
        form = AddFieldForm(request.GET)
        if form.is_valid():
            field_type_pk = form.cleaned_data['field_type']

            modelo_pk = self.kwargs.get('modelo_pk', None)
            model_defs = models.ModelDefinition.objects.filter(pk=modelo_pk)

            self.form_class = get_field_def_form(field_type_pk, model_defs)
            self.model = get_mutant_type(field_type_pk)
            self.initial = {'model_def': modelo_pk,
                            'content_type': field_type_pk}
            return super_func()
        else:
            return redirect(self.get_success_url())

    def get(self, request, modelo_pk):
        super_func = lambda: super(CampoCriaView, self).get(request, modelo_pk)
        return self._prepare_dynamic_form(request, modelo_pk, super_func)

    def post(self, request, modelo_pk):
        super_func = lambda: super(CampoCriaView, self).post(request, modelo_pk)
        return self._prepare_dynamic_form(request, modelo_pk, super_func)


criar_campo = CampoCriaView.as_view()


class CampoEditaView(SuccessUrlMixin, UpdateView):
    template_name = 'sistema/field_save.html'

    def get_success_url(self):
        self.success_url = self.get_reversed_success_url()
        return super(CampoEditaView, self).get_success_url()

    def get_object(self):
        modelo_pk = self.kwargs.get('modelo_pk', None)
        model_defs = models.ModelDefinition.objects.filter(pk=modelo_pk)

        field_pk = self.kwargs.get('field_pk', None)
        base_field = get_object_or_404(models.FieldDefinition, pk=field_pk)
        field_type_pk = base_field.type_cast().get_content_type().pk

        self.form_class = get_field_def_form(field_type_pk, model_defs)
        self.model = get_mutant_type(field_type_pk)

        field = self.model.objects.get(pk=field_pk)

        return field


editar_campo = CampoEditaView.as_view()


class CampoExcluiView(SuccessUrlMixin, DeleteView):
    model = models.FieldDefinition
    template_name = 'sistema/field_delete.html'

    def delete(self, *args, **kwargs):
        self.success_url = self.get_reversed_success_url()
        return super(CampoExcluiView, self).delete(*args, **kwargs)


excluir_campo = CampoExcluiView.as_view()

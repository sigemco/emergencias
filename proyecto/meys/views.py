from .models import Photo
from .forms import PhotoForm
from django.shortcuts import render, redirect

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from .models import Documento

from django.urls import reverse

from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

from django import forms

from django.contrib.admin.widgets import AdminDateWidget

# para el ejemplo de subir archivos ajax
from django.http import JsonResponse
from django.views import View
import time

from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    return render(request, 'meys/indexmeys.html')


class BasicUploadView(View):
    def get(self, request):
        photos_list = Photo.objects.all()
        return render(self.request, 'meys/basic_upload/index.html', {'photos': photos_list})

    def post(self, request):
        form = PhotoForm(self.request.POST, self.request.FILES)
        if form.is_valid():
            photo = form.save()
            data = {'is_valid': True, 'name': photo.file.name,
                    'url': photo.file.url}
        else:
            data = {'is_valid': False}
        return JsonResponse(data)


class ProgressBarUploadView(View):
    def get(self, request):
        photos_list = Photo.objects.all()
        return render(self.request, 'meys/progress_bar_upload/index.html', {'photos': photos_list})

    def post(self, request):
        # You don't need this line. This is just to delay the process so you can see the progress bar testing locally.
        time.sleep(1)
        form = PhotoForm(self.request.POST, self.request.FILES)
        if form.is_valid():
            photo = form.save()
            data = {'is_valid': True, 'name': photo.file.name,
                    'url': photo.file.url}
        else:
            data = {'is_valid': False}
        return JsonResponse(data)


class DragAndDropUploadView(View):
    def get(self, request):
        photos_list = Photo.objects.all()
        return render(self.request, 'meys/drag_and_drop_upload/index.html', {'photos': photos_list})

    def post(self, request):
        form = PhotoForm(self.request.POST, self.request.FILES)
        if form.is_valid():
            photo = form.save()
            data = {'is_valid': True, 'name': photo.file.name,
                    'url': photo.file.url}
        else:
            data = {'is_valid': False}
        return JsonResponse(data)


def clear_database(request):
    for photo in Photo.objects.all():
        photo.file.delete()
        photo.delete()
    return redirect('basic_upload')

# https://www.agiliq.com/blog/2019/01/django-formview/ -- Si bien no untilizo esto aca esta muy bueno lo q se puede hacer


class DocumentoInicio(TemplateView):
    template_name = "inicio.html"
    """
    #https://www.agiliq.com/blog/2017/12/when-and-how-use-django-templateview/
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['documentos'] = Documento.objects.all()
        return context
    """


class DocumentosListado(ListView):
    model = Documento
    """
    #https://www.agiliq.com/blog/2017/12/when-and-how-use-django-listview/
    #para pasar una variable al context personalizada
    def get_context_data(self, *args, **kwargs):
    		context = super(DocumentosListado, self).get_context_data(*args, **kwargs)
		context['documentos'] = Documento.objects.all()
		return context
    """
    """
    #También podemos agregar filtros en ListView.queryset.
    queryset = Documento.objects.filter(documento='3T20')#En caso de no neceisar consultas, usar model = Documento solamente sin queryset
	context_object_name = 'documento'
    paginate_by = 10
    """


class DocumentoVer(DetailView):
    model = Documento
    # https://www.agiliq.com/blog/2019/01/django-when-and-how-use-detailview/


class DocumentoCrear(SuccessMessageMixin, CreateView):
    # http://melardev.com/blog/2017/11/04/createview-django-4-examples --> puede servir para acceder a la instancia del modelo y asiganr permisos
    model = Documento
    #form = Documento
    fields = "__all__"

    """
    #Agregar datos iniciales a CreateView
    #https://www.agiliq.com/blog/2019/01/django-createview/
    def get_initial(self, *args, **kwargs):
        initial = super(DocumentoCrear, self).get_initial(**kwargs)
        initial['documento'] = 'documento'
        initial['destino'] = 'destino'
        return initial
    
    def get_form(self):
        form = super().get_form()
        form.fields['termino'].widget = DateTimePickerInput()
        return form
        #attrs = AdminDateWidget
    """

    # Mostramos este Mensaje luego de Crear un Documento
    success_message = 'Documento creado correctamente !'

    # Redireccionamos a la página principal luego de crear un registro o documento
    def get_success_url(self):
        # Redireccionamos a la vista principal 'listar'
        return reverse('listarDocumento')


class DocumentoEditar(SuccessMessageMixin, UpdateView):
    model = Documento
    form = Documento
    fields = "__all__"
    # Mostramos este Mensaje luego de Editar un Documento
    success_message = 'Documento actualizado correctamente !'

    # Redireccionamos a la página principal luego de actualizar un registro o documento
    def get_success_url(self):
        # Redireccionamos a la vista principal 'listar'
        return reverse('listarDocumento')


class DocumentoEliminar(SuccessMessageMixin, DeleteView):
    model = Documento
    form = Documento
    fields = "__all__"

    # Redireccionamos a la página principal luego de eliminar un registro o documento
    def get_success_url(self):
        # Mostramos este Mensaje luego de Editar un Documento
        success_message = 'Documento eliminado correctamente !'
        messages.success(self.request, (success_message))
        # Redireccionamos a la vista principal 'listar'
        return reverse('listarDocumento')

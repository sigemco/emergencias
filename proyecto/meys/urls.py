
from django.urls import path
from .views import index, DocumentoCrear, DocumentoVer, DocumentoEliminar, DocumentosListado, DocumentoEditar, DocumentoInicio, clear_database, BasicUploadView, ProgressBarUploadView, DragAndDropUploadView


urlpatterns = [
    path('', index, name='indexmeys'),
    path('inicio/', DocumentoInicio.as_view(template_name="meys/inicio.html"),
         name='inicioDocumento'),
    path('documentos/listado', DocumentosListado.as_view(
        template_name="meys/listado.html"), name='listarDocumento'),
    path('documentos/ver/<int:pk>',
         DocumentoVer.as_view(template_name="meys/ver.html"), name='verDocumento'),
    path('documentos/crear', DocumentoCrear.as_view(template_name="meys/crear.html"),
         name='crearDocumento'),
    path('documentos/editar/<int:pk>', DocumentoEditar.as_view(
        template_name="meys/editar.html"), name='editarDocumento'),
    path('documentos/eliminar/<int:pk>',
         DocumentoEliminar.as_view(), name='eliminarDocumento'),
    # path para subir archivos
    path('clear/', clear_database, name='clear_database'),
    path('basic-upload/', BasicUploadView.as_view(), name='basic_upload'),
    path('progress-bar-upload/', ProgressBarUploadView.as_view(),
         name='progress_bar_upload'),
    path('drag-and-drop-upload/', DragAndDropUploadView.as_view(),
         name='drag_and_drop_upload'),
]

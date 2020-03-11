from django.contrib import admin
from .models import Documento


@admin.register(Documento)
class EstadoAdmin(admin.ModelAdmin):
    list_display = ('destino', 'documento', 'termino')

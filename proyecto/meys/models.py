from django.db import models
from django.utils import timezone

# Creación de campos de la tabla 'postres'


class Documento(models.Model):
    destino = models.CharField(max_length=20, null=False)
    documento = models.CharField(max_length=100, null=False)
    archivo = models.FileField(upload_to='archivos/')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    termino = models.DateTimeField('termino')

    class Meta:
        db_table = 'documento'

    def __str__(self):
        return 'documento'


class Photo(models.Model):
    title = models.CharField(max_length=255, blank=True)
    file = models.FileField(upload_to='archivos/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

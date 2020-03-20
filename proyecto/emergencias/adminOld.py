from django.contrib import admin
from .models import Estado, Persona, Grado, Especialidad, TipOperacion, TipoTransporte,  Medios, CentroSalud, Efectos, OperacionesEnDesarrollo, Unidades
from datetime import datetime
from django.http import HttpResponse
from io import BytesIO
from django.conf import settings

from leaflet.admin import LeafletGeoAdmin

@admin.register(Unidades)
class UnidadesAdmin(admin.ModelAdmin):
    list_display = ('unidad',)

@admin.register(TipOperacion)
class TipoOeracionAdmin(admin.ModelAdmin):
    list_display = ('tipo',)

@admin.register(TipoTransporte)
class TipoTransporteAdmin(admin.ModelAdmin):
    list_display = ('tipotransporte',)
    search_fields = ['tipotransporte']

@admin.register(Medios)
class MediosAdmin(admin.ModelAdmin):
    list_display = ('medio',)

@admin.register(CentroSalud)
class CentroSaludAdmin(admin.ModelAdmin):
    list_display = ('centro',)
    search_fields = ['centro']


@admin.register(Efectos)
class EfectosAdmin(admin.ModelAdmin):
    list_display = ('efecto','unidad',)
    search_fields = ['efecto']

"""
@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha_nacimiento',)
    search_fields = ['nombre']
    autocomplete_fields = ['especialidad',]
"""
class PersonaAdmin(LeafletGeoAdmin):
    list_display = ('nombre', 'fecha_nacimiento',)
    search_fields = ['nombre']
    autocomplete_fields = ['especialidad',]

admin.site.register(Persona, PersonaAdmin)

@admin.register(Grado)
class GradoAdmin(admin.ModelAdmin):
    list_display = ('grado',)

@admin.register(Especialidad)
class EspecialidadAdmin(admin.ModelAdmin):
    list_display = ('especialidad',)
    search_fields = ['especialidad']

@admin.register(OperacionesEnDesarrollo)
class OperacionesEnDesarrolloAdmin(admin.ModelAdmin):
    list_display = ('titulo','mision','objetivo','tipoperacion')
    autocomplete_fields = ['efectos','centrosalud', 'personal','tipotransporte']



@admin.register(Estado)
class EstadoAdmin(admin.ModelAdmin):
    list_display = ('user', 'status',)
# https://stackoverflow.com/questions/51347371/django-admin-export-to-pdf?answertab=active#tab-top
    actions = ["exportar_a_pdf"]

    def exportar_a_pdf(self, request, queryset):

        file_name = "prueba-{0}.pdf".format(
            datetime.now().strftime('%d-%m-%Y-%H-%M-%S'))
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="{0}"'.format(
            file_name)

        buffer = BytesIO()
        pdf = canvas.Canvas(buffer, pagesize=A4)
        archivo_imagen = settings.MEDIA_ROOT+'/imagenes/django_logo.png'
        pdf.drawImage(archivo_imagen, 40, 750, 120,
                      90, preserveAspectRatio=True)
        pdf.setFont("Helvetica", 16)
        pdf.drawString(230, 790, u"MEYS Secr Ayte JEMCO")
        pdf.setFont("Helvetica", 14)
        pdf.drawString(270, 770, u"Hoja de Ruta")
        pdf.setFont("Helvetica-Bold", 14)
        pdf.drawString(480, 750, datetime.now().strftime('%d/%m/%Y'))
        pdf.line(460, 747, 560, 747)

        pdf.showPage()
        pdf.save()
        pdf = buffer.getvalue()
        buffer.close()
        response.write(pdf)

        return response
    exportar_a_pdf.short_description = "Imprimir Hoja de Ruta en PDF"

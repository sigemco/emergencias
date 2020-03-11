from django.contrib import admin
from .models import Estado
from datetime import datetime
from django.http import HttpResponse
from io import BytesIO
from django.conf import settings



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

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from core.models import UserSigemco
from django.http import HttpResponse
from datetime import datetime

#Importamos settings para poder tener a la mano la ruta de la carpeta media
from django.conf import settings
from io import BytesIO

from django.views.generic import View
from core.models import UserSigemco




# Create your views here.
@login_required
def vistaIndex(request):
    return render(request, 'indexelecciones.html')
def vistaVideo(request):
    return render(request, 'video.html')

def usuarios(request):
    users = UserSigemco.objects.all()
    return render(request, 'usuarios.html', {'users': users})


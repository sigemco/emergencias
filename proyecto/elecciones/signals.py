# A TENER EN CUENTA: Para q este archivo sea reconocido agregar la siguiente línea en INSTALLED_APPS:
# nombre_de_la_aplicacion.apps.AplicacionConfig
# Si se tiene un modelo personalizado (En este caso UserSigemco), para que reconozca todo borrar la BD
# y ejecutar las migraciones, sino no reconoce dicho modelo. Más aún si el modelo personalizado
# esta en otra aplicación como acá q esta en core.models

# https://sodocumentation.net/es/django/topic/2555/senales

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
#from django.contrib.auth.models import User
from core.models import UserSigemco
from django.template.loader import render_to_string
from .models import Estado


@receiver(post_delete, sender=UserSigemco)
@receiver(post_save, sender=UserSigemco)
def change_user(sender, instance, *args, **kwargs):
    users = UserSigemco.objects.all()
    html_users = render_to_string("modificar_estado_usuarios.html", {
                                  'users': users, 'currect_user': instance.username})

    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "users",
        {
            "type": "user_update",
            "event": "New User",
                    'html_users': html_users,
        }
    )


@receiver(post_save, sender=UserSigemco)
def new_user(sender, instance, created, **kwargs):
    if created:
        Estado.objects.create(user=instance)

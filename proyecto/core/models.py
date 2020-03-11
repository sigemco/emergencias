from django.db import models
from django.contrib.auth.models import AbstractUser


class UserSigemco(AbstractUser):
    # Devuelve una lista de Roles del usuario autenticado
    """
    def permisos(self):
        from apps.usuarios.models import Role
        grup = self.groups.all()
        lista_rol_en_grupo = []
        # Listado de roles por grupo
        dato_del_usuario = {'grupos': [w.name for w in grup]}
        # dato_del_usuario = {}
        for x in grup:
            a = Role.objects.filter(grupos=x)
            lista_rol_en_grupo += [z.nombre for z in a]

        # Listado de roles del usuario
        acl = Role.objects.filter(usuarios=self)
        # Set devulve una lista sin valores repetidos
        dato_del_usuario['roles'] = list(set(lista_rol_en_grupo + [y.nombre for y in acl if acl]))
        return json.dumps(dato_del_usuario)
    """

    def __str__(self):
        return self.username

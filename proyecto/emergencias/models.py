from django.db import models
from django.conf import settings


class Estado(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='estado')
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"Estado de {self.user.username}"

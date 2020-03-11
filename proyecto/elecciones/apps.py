from django.apps import AppConfig


class EleccionesConfig(AppConfig):
    name = 'elecciones'

    def ready(self):
        from . import signals

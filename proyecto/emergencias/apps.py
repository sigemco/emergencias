from django.apps import AppConfig


class EmergenciasConfig(AppConfig):
    name = 'emergencias'

    def ready(self):
        from . import signals

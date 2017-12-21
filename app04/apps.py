from django.apps import AppConfig
from django.utils.module_loading import autodiscover_modules

class App04Config(AppConfig):
    name = 'app04'
    def ready(self):
        autodiscover_modules('stark')

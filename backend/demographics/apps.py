from django.apps import AppConfig
from .tasks import scheduler

class DemographicsConfig(AppConfig):
    #default_auto_field = 'django.db.models.BigAutoField'
    name = 'demographics'

    def ready(self):
        if not scheduler.running:  
            scheduler.start()
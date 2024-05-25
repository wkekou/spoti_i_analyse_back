from django.apps import AppConfig
from django_cron import CronJobBase, Schedule


class SpotifyConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'spotify'
    
    def ready(self):
        from .cron import FetchSpotifyDataCronJob

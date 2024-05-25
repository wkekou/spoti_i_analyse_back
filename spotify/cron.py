from django_cron import CronJobBase, Schedule
from .utils import fetch_spotify_data

class FetchSpotifyDataCronJob(CronJobBase):
    RUN_EVERY_MINS = 60  # Exécuter toutes les heures

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'spotify.fetch_spotify_data_cron_job'  # Identificateur unique pour cette tâche cron

    def do(self):
        fetch_spotify_data()

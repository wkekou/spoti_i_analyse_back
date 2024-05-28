from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab


# Définir le module de configuration Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myspotifyapp.settings')

app = Celery('myspotifyapp')

# Utiliser une chaîne ici signifie que le worker n'a pas
# besoin de sérialiser la configuration de l'objet.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Charger les tâches des applications Django enregistrées
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    from spotify.tasks import fetch_spotify_data_task  # Assurez-vous que cette ligne est présente
    # Appelle update_spotify_data_task toutes les minutes pour les tests
    sender.add_periodic_task(
        crontab(minute='*/1'),  # Pour tester toutes les minutes
        fetch_spotify_data_task.s(),
    )
from __future__ import absolute_import, unicode_literals
import logging
from celery import Celery, shared_task
from celery.schedules import crontab
from .utils import fetch_spotify_data


logger = logging.getLogger(__name__)

@shared_task
def update_spotify_data_task():
    logger.info("Fetching Spotify data...")
    fetch_spotify_data()
    logger.info("Data fetch complete.")

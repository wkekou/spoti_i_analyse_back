from __future__ import absolute_import, unicode_literals
from celery import shared_task
import logging
from .utils import fetch_spotify_data

logger = logging.getLogger(__name__)

@shared_task
def fetch_spotify_data_task():
    
    try:
        logger.info("Fetching Spotify data...")
        fetch_spotify_data()
        logger.info("Data fetch complete.")
    except Exception as e:
        logger.error(f"Error in fetch_spotify_data_task : {e}")
        raise e

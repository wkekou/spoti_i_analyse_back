import spotipy
from spotipy.oauth2 import SpotifyOAuth
from .models import RecentTrack, TopArtist, TopTrack, Genre, TopGenre, ListeningHistory
from django.conf import settings
from datetime import datetime
import pytz
import logging

logger = logging.getLogger(__name__)

def fetch_spotify_data():
    logger.info("Starting fetch_spotify_data")
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=settings.SPOTIFY_CLIENT_ID,
                                                   client_secret=settings.SPOTIFY_CLIENT_SECRET,
                                                   redirect_uri=settings.SPOTIFY_REDIRECT_URI,
                                                   scope='user-read-recently-played user-top-read'))

    # Récupérer les morceaux récemment écoutés
    try:
        recent_tracks = sp.current_user_recently_played(limit=50)
        for item in recent_tracks['items']:
            track = item['track']
            played_at = datetime.strptime(item['played_at'], "%Y-%m-%dT%H:%M:%S.%fZ").replace(tzinfo=pytz.UTC)
            artist = track['artists'][0]
            artist_image = artist['images'][0]['url'] if artist['images'] else ''
            logger.info(f"Saving track: {track['name']} by {artist['name']}")
            
            # Enregistrement dans RecentTrack          
            RecentTrack.objects.get_or_create(
                name=track['name'],
                artist=artist['name'],
                artist_image=artist_image,
                played_at=played_at
            )
            # Enregistrement dans ListeningHistory
            ListeningHistory.objects.create(
                name=track['name'],
                artist=artist['name'],
                artist_image=artist_image,
                played_at=played_at
            )            
            
    except Exception as e:
        logger.error(f"Error fetching recent tracks: {e}")

    # Récupérer les artistes les plus écoutés
    try:
        top_artists = sp.current_user_top_artists(limit=10)
        followed_artists = sp.current_user_followed_artists(limit=50)['artists']['items']
        followed_artists_ids = {artist['id'] for artist in followed_artists}
        
        for artist in top_artists['items']:
            logger.info(f"Saving artist: {artist['name']}")
            is_followed = artist['id'] in followed_artists_ids
            TopArtist.objects.get_or_create(
                name=artist['name'],
                image_url=artist['images'][0]['url'] if artist['images'] else '',
                description=artist['bio'] if 'bio' in artist else '',
                is_followed=is_followed,
                popularity=artist['popularity']
            )
    except Exception as e:
        logger.error(f"Error fetching top artists: {e}")

    # Récupérer les morceaux les plus écoutés
    try:
        top_tracks = sp.current_user_top_tracks(limit=10)
        for track in top_tracks['items']:
            artist = track['artists'][0]
            artist_image = artist['images'][0]['url'] if artist['images'] else ''
            logger.info(f"Saving track: {track['name']} by {artist['name']}")
            TopTrack.objects.get_or_create(
                name=track['name'],
                artist=artist['name'],
                artist_image=artist_image,
                played_at=track['played_at'],  # Assurez-vous d'ajouter cette information dans le backend
                popularity=track['popularity']
            )
    except Exception as e:
        logger.error(f"Error fetching top tracks: {e}")

    # Récupérer les genres les plus écoutés
    try:
        genres = sp.recommendation_genre_seeds()
        for genre in genres['genres']:
            logger.info(f"Saving genre: {genre}")
            genre_obj, created = Genre.objects.get_or_create(name=genre)
            if created:
                TopGenre.objects.get_or_create(genre=genre_obj, count=0)
            else:
                top_genre = TopGenre.objects.get(genre=genre_obj)
                top_genre.count += 1
                top_genre.save()
    except Exception as e:
        logger.error(f"Error fetching genres: {e}")

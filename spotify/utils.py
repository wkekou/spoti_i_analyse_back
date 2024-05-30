import logging
import datetime
import pytz
import spotipy
from django.conf import settings
from spotipy.oauth2 import SpotifyOAuth
from .models import RecentTrack, TopArtist, TopTrack, Genre, TopGenre, ListeningHistory

logger = logging.getLogger(__name__)

def get_recenttracks_listeninghistory_genre(sp):
    """_Récupérer les morceaux récemment écoutés. On ne peut récupérer que les 50 dernières écoutes_
    _De cette récupération, on enregistre une copie dans la table historisée_
    _Puis on récupère les genres des musiques et le top 10_

    Args:
        sp (_spotipy.Spotify_): _Spotify class from spotipy. Used to interact with spotify api object_
    """
    try:
        recent_tracks = sp.current_user_recently_played(limit=50)
        genres_count = {}
        for item in recent_tracks['items']:
            track = item['track']
            played_at = datetime.datetime.strptime(item['played_at'], "%Y-%m-%dT%H:%M:%S.%fZ").replace(tzinfo=pytz.UTC)
            artist = track['artists'][0]
            # On récupère la photo de l'artiste
            search_tmp = sp.search(q='artist:' + artist['name'], type='artist')
            res_tmp = search_tmp['artists']['items']
            if len(res_tmp)>0:
                artist_tmp = res_tmp[0]
                artist_image = artist_tmp['images'][0]['url']
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
            # Récupérer les genres des artistes des morceaux récemment écoutés
            artist_genres = sp.artist(artist['id'])['genres']
            for genre in artist_genres:
                if genre in genres_count:
                    genres_count[genre] += 1
                else:
                    genres_count[genre] += 1
            
            
            for genre, count in genres_count.items():
                logger.info(f"Saving genre: {genre}")
                genre_obj, created = Genre.objects.get_or_create(name=genre)
                if created:
                    TopGenre.objects.create(genre=genre_obj, count=count)
                else:
                    top_genre = TopGenre.objects.get(genre=genre_obj)
                    top_genre.count += count
                    top_genre.save()
            
            
    except Exception as e:
        logger.error(f"Error on function get_recenttracks_listeninghistory_genre: {e}")


def get_toptrackartist(sp):
    """_Récupérer les artistes les plus écoutés. Provient directement de l'api spotify_

    Args:
        sp (_spotipy.Spotify_): _Spotify class from spotipy. Used to interact with spotify api object_
    """
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


def get_toptracks(sp):
    """_Récupérer les morceaux les plus écoutés. Principalement le Top 10_

    Args:
        sp (_spotipy.Spotify_): _Spotify class from spotipy. Used to interact with spotify api object_
    """
    # Récupérer les morceaux les plus écoutés
    try:
        top_tracks = sp.current_user_top_tracks(limit=10)
        for track in top_tracks['items']:
            artist = track['artists'][0]            
            # On récupère la photo de l'artiste
            search_tmp = sp.search(q='artist:' + artist['name'], type='artist')
            res_tmp = search_tmp['artists']['items']
            if len(res_tmp)>0:
                artist_tmp = res_tmp[0]
                artist_image = artist_tmp['images'][0]['url']
            logger.info(f"Saving track: {track['name']} by {artist['name']}")
            TopTrack.objects.get_or_create(
                name=track['name'],
                artist=artist['name'],
                artist_image=artist_image,
                popularity=track['popularity']
            )
    except Exception as e:
        logger.error(f"Error fetching top tracks: {e}")


def fetch_spotify_data():
    """_Récupérer les données spotify pour les agréger dans la base de données_
    """
    logger.info("Starting fetch_spotify_data")
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=settings.SPOTIFY_CLIENT_ID,
                                                   client_secret=settings.SPOTIFY_CLIENT_SECRET,
                                                   redirect_uri=settings.SPOTIFY_REDIRECT_URI,
                                                   scope='user-read-recently-played user-top-read'))
    get_recenttracks_listeninghistory_genre(sp=sp)
    get_toptrackartist(sp=sp)
    get_toptracks(sp=sp)
    print("Spotify data fetched successfully")
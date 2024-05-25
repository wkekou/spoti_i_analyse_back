from django.http import HttpResponse, JsonResponse
from rest_framework import generics
from .models import RecentTrack, TopArtist, TopTrack, ListeningHistory, TopGenre, Genre
from .serializers import RecentTrackSerializer, TopArtistSerializer, TopTrackSerializer, ListeningHistorySerializer, TopGenreSerializer, GenreSerializer
from .utils import fetch_spotify_data


def home(request):
    return HttpResponse("Bienvenue sur l'application Spoti-I-Analyse")

def update_spotify_data(request):
    fetch_spotify_data()
    return JsonResponse({'status': 'success'})


class RecentTrackList(generics.ListCreateAPIView):
    queryset = RecentTrack.objects.all()
    serializer_class = RecentTrackSerializer

class TopArtistList(generics.ListCreateAPIView):
    queryset = TopArtist.objects.all()
    serializer_class = TopArtistSerializer

class TopTrackList(generics.ListCreateAPIView):
    queryset = TopTrack.objects.all()
    serializer_class = TopTrackSerializer

class ListeningHistoryList(generics.ListCreateAPIView):
    queryset = ListeningHistory.objects.all()
    serializer_class = ListeningHistorySerializer
    
class GenreList(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class TopGenreList(generics.ListCreateAPIView):
    queryset = TopGenre.objects.all()
    serializer_class = TopGenreSerializer

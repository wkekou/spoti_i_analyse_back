from django.http import HttpResponse, JsonResponse
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
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

class ListeningHistoryList(generics.ListAPIView):
    queryset = ListeningHistory.objects.all().order_by('-played_at')
    serializer_class = ListeningHistorySerializer
    pagination_class = PageNumberPagination
    
class GenreList(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    pagination_class = PageNumberPagination  # Utilisez la pagination


class TopGenreList(generics.ListCreateAPIView):
    queryset = TopGenre.objects.all().order_by('-count')[:10]  # Limitez à 10 genres les plus écoutés
    serializer_class = TopGenreSerializer

from django.urls import path
from . import views

urlpatterns = [
    path('recent-tracks/', views.RecentTrackList.as_view(), name='recent-tracks'),
    path('top-artists/', views.TopArtistList.as_view(), name='top-artists'),
    path('top-tracks/', views.TopTrackList.as_view(), name='top-tracks'),
    path('listening-history/', views.ListeningHistoryList.as_view(), name='listening-history'),
    path('genres/', views.GenreList.as_view(), name='genres'),
    path('top-genres/', views.TopGenreList.as_view(), name='top-genres'),
    path('update-spotify-data/', views.update_spotify_data, name='update-spotify-data'),
]

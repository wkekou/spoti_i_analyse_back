from rest_framework import serializers
from .models import RecentTrack, TopArtist, TopTrack, ListeningHistory, TopGenre, Genre

class RecentTrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecentTrack
        fields = ['name', 'artist', 'artist_image', 'played_at']

class TopArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopArtist
        fields = ['name', 'image_url', 'description', 'is_followed', 'popularity']

class TopTrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopTrack
        fields = ['name', 'artist', 'artist_image', 'played_at', 'popularity']

class ListeningHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ListeningHistory
        fields = '__all__'

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['name']

class TopGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopGenre
        fields = ['genre', 'count']

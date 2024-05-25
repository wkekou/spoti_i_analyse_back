from rest_framework import serializers
from .models import RecentTrack, TopArtist, TopTrack, ListeningHistory, TopGenre, Genre

class RecentTrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecentTrack
        fields = '__all__'

class TopArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopArtist
        fields = '__all__'

class TopTrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopTrack
        fields = '__all__'

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

from django.db import models

class RecentTrack(models.Model):
    name = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    artist_image = models.URLField(max_length=200, blank=True)
    played_at = models.DateTimeField()

class TopArtist(models.Model):
    name = models.CharField(max_length=255)
    popularity = models.IntegerField()

class TopTrack(models.Model):
    name = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    popularity = models.IntegerField()

class ListeningHistory(models.Model):
    track = models.ForeignKey(RecentTrack, on_delete=models.CASCADE)
    count = models.IntegerField()

class Genre(models.Model):
    name = models.CharField(max_length=255)

class TopGenre(models.Model):
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    count = models.IntegerField(default=0)

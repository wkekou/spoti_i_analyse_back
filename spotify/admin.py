from django.contrib import admin
from .models import RecentTrack, TopArtist, TopTrack, ListeningHistory, TopGenre, Genre

admin.site.register(RecentTrack)
admin.site.register(TopArtist)
admin.site.register(TopTrack)
admin.site.register(ListeningHistory)
admin.site.register(Genre)
admin.site.register(TopGenre)

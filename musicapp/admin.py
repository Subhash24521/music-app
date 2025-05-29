from django.contrib import admin

from musicapp.models import Artist, Playlist, movies

# Register your models here.
admin.site.register(Artist)
admin.site.register(movies)
admin.site.register(Playlist)
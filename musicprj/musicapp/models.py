from django.db import models
from django.contrib.auth.models import User

class Artist(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField()

    def __str__(self):
        return self.name

class movies(models.Model):
    name=models.CharField(max_length=100)
    thumbnail=models.ImageField()
    description=models.TextField()
    lyrics=models.TextField()
    choosevideo = models.FileField(max_length=60, upload_to="audios")
    def __str__(self):
        return self.name+str(self.id)

class Playlist(models.Model):
    name = models.CharField(max_length=200)  # Name of the song or video
    file = models.FileField(upload_to="media/")  # Store audio or video files here
    file_type = models.CharField(
        max_length=10,
        choices=[('audio', 'Audio'), ('video', 'Video')],
        default='audio'
    )  # Differentiating between audio and video
    duration = models.IntegerField(default=0)  # Duration of the media item in seconds (optional)

    def __str__(self):
        return f"{self.name} ({self.file_type})"




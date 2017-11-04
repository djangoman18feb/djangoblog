from django.db import models

# Create your models here.

class Album(models.Model):
    album_title = models.CharField(max_length=50)
    logo = models.CharField(max_length=200)
    genre = models.CharField(max_length=50)
    Artist = models.CharField(max_length=200)

    def __str__(self):
        return self.album_title + '-' + self.Artist

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=50)
    song_title = models.CharField(max_length=200)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title + '-' + self.file_type



from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=256)

    def __str__(self):
        return self.display_name

class Artist(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name
    
class Album(models.Model):
    artist = models.ForeignKey('Artist', on_delete=models.CASCADE)
    name = models.CharField(max_length=256)

    def __str__(self):
        return f'{self.name} by {self.name}'
    
class Track(models.Model):
    album = models.ForeignKey('Album', on_delete=models.CASCADE)
    name = models.CharField(max_length=256)

    def __str__(self):
        return f'{self.name} by {self.album.artist.name}'
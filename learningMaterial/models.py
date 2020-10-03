from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Blurb(models.Model):
    blurbText = models.TextField(max_length=5000)
    fromLink = models.URLField(max_length=600)

class YoutubeVideo(models.Model):
    link = models.URLField(max_length=600)
    favorites = models.IntegerField()

class LectureNote(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField()
    favorites = models.IntegerField()


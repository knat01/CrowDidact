from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

# Create your models here.

alphanumeric = RegexValidator(r'^[0-9a-zA-Z _]*$', 'Only alphanumeric, spaces, and underscores may be included')

class Subject(models.Model):
    name = models.CharField(max_length=150, unique=True, validators=[alphanumeric])

    def __str__(self):
        return self.name

    def humanRead(self):
        return self.name.replace('_', ' ')

class Blurb(models.Model):
    blurbText = models.TextField(max_length=50000)
    fromLink = models.URLField(max_length=600, null=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="blurb")
    def __str__(self):
        return self.subject.name

class YoutubeVideo(models.Model):
    link = models.URLField(max_length=600)
    favorites = models.IntegerField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.link

class LectureNote(models.Model):
    title = models.CharField(max_length=80,default="Note",blank=True,null=True,unique=True,validators=[alphanumeric])
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField()
    favorites = models.IntegerField(default=0)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def humanRead(self):
        return self.title.replace('_', ' ')
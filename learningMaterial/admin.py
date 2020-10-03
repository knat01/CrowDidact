from django.contrib import admin
from .models import LectureNote,YoutubeVideo,Blurb,Subject

# Register your models here.
admin.site.register(LectureNote)
admin.site.register(YoutubeVideo)
admin.site.register(Blurb)
admin.site.register(Subject)
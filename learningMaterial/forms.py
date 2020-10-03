from django.forms import ModelForm
from .models import LectureNote

class uploadNoteForm(ModelForm):
    class Meta:
        model = LectureNote
        fields = ['title','image','subject','author','favorites']
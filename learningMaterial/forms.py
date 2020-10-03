from django.forms import ModelForm
from .models import LectureNote, Subject

class uploadNoteForm(ModelForm):
    class Meta:
        model = LectureNote
        fields = ['title','image','subject','author','favorites']


class createSubjectForm(ModelForm):
    class Meta:
        model = Subject
        fields = ["name"]
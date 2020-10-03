from django.shortcuts import render
from .models import Subject
from django.http import HttpResponse

subDummy = Subject.objects.all().first()

def subject(request):
    return render(request,"subjectBase.html",{subject:subDummy})


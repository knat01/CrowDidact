from django.shortcuts import render
from .models import Subject, LectureNote
from django.http import HttpResponse
from .forms import uploadNoteForm, createSubjectForm
from django.http import HttpResponseRedirect
from django.urls import reverse

sub = Subject.objects.all().first()

def subject(request, subjectStr):
    if subjectStr:
        sub = Subject.objects.get(name__icontains=subjectStr)
    return render(request,"subjectBase.html",{"subject":sub})

def note(request, noteStr):
    note = LectureNote.objects.get(title__iexact=noteStr)
    return render(request,"note.html",{"note":note})

def upload(request):

    if request.method == "POST":
        form = uploadNoteForm(request.POST, request.FILES, request.user)
        
        if form.is_valid():
            newTitle = form.cleaned_data["title"].replace(" ","_")
            obj = LectureNote(image=form.cleaned_data["image"],subject = form.cleaned_data["subject"],favorites=0,title=newTitle,author=request.user)
            obj.save()
            
            return HttpResponseRedirect(reverse(subject, args=[form.cleaned_data["subject"].name.split(' ', 1)[0]]))
        
    else:
        form = uploadNoteForm()

    context = {
        'form':form
    }

    return render(request,"./form.html",context)

def newSubject(request):
    if request.method == "POST":
        form = createSubjectForm(request.POST, request.user)
        
        if form.is_valid():

            obj = Subject(form.cleaned_data["name"].replace(" ","_"))
            obj.save()
            
            
            return HttpResponseRedirect(reverse(subject, args=[form.cleaned_data['name']]))
        
    else:
        form = createSubjectForm()

    context = {
        'form':form
    }

    return render(request,"./form.html",context)

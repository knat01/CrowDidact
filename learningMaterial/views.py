from django.shortcuts import render
from .models import Subject, LectureNote
from django.http import HttpResponse
from .forms import uploadNoteForm
from django.http import HttpResponseRedirect


subDummy = Subject.objects.all().first()

def subject(request):
    return render(request,"subjectBase.html",{"subject":subDummy})

def upload(request):

    if request.method == "POST":
        form = uploadNoteForm(request.POST, request.FILES, request.user)
        
        if form.is_valid():
            new = LectureNote(request.FILES['image'],form.subject,form.favorites,form.title,form.author)
            new.save()
            
            return HttpResponseRedirect("learningMaterials")
        
    else:
        form = uploadNoteForm()

    context = {
        'form':form
    }

    return render(request,"./uploadNote.html",context)
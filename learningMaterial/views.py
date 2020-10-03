from django.shortcuts import render
from .models import Subject, LectureNote
from django.http import HttpResponse
from .forms import uploadNoteForm
from django.http import HttpResponseRedirect


sub = Subject.objects.all().first()

def subject(request, subjectStr):
    if subjectStr:
        sub = Subject.objects.get(name__icontains=subjectStr)
    return render(request,"subjectBase.html",{"subject":sub})

def upload(request):

    if request.method == "POST":
        form = uploadNoteForm(request.POST, request.FILES, request.user)
        
        if form.is_valid():
            form.save()
            
            
            return HttpResponseRedirect("learningMaterials")
        
    else:
        form = uploadNoteForm()

    context = {
        'form':form
    }

    return render(request,"./uploadNote.html",context)
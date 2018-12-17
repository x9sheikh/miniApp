from django.shortcuts import render
from django.http import HttpResponse
from .models import Subject, MySmartNote, Mentor
from .forms import CreateForm
# Create your views here.
def index(request):
    context = {
        'myNotes': MySmartNote.objects.all()
    }
    return render(request,'smartNotes/index.html', context)

def detailNotes(request, notesId):
    thisNote = MySmartNote.objects.get(id=notesId)
    context = {
        'title': thisNote.title,
        'notesId': notesId
    }
    return render(request,'smartNotes/detailNotes.html', context)

def createNotes(request):
    form = CreateForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            title = form.cleaned_data['title']
            subject = form.cleaned_data['subject']
            mentor = form.cleaned_data['mentor']
            context = form.cleaned_data['context']
            mentorObject = Mentor.objects.create(name=mentor)
            mentorObject.save()
            subjectObject = Subject.objects.create(name=subject)
            subjectObject.save()
            mySmartNoteObject = MySmartNote.objects.create(
                title=title,
                subject=subjectObject,
                mentor=mentorObject,
                context=context
            )
            mySmartNoteObject.save()
            return HttpResponse("Success")
        else:
            print ("NonSuccess")
            return HttpResponse("UnSuccess")
    else:
        context = {
            'form': form
        }
        return render(request, 'smartNotes/createNotes.html', context)
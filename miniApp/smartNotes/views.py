from django.shortcuts import render
from django.http import HttpResponse
from .models import Subject, SmartNotes, Mentor
from .forms import CreateForm
# Create your views here.
def index(request):
    context = {
        'myNotes': SmartNotes.objects.all()
    }
    return render(request,'smartNotes/index.html', context)

def detailNotes(request, notesId):
    thisNote = SmartNotes.objects.get(id=notesId)
    context = {
        'title': thisNote.title,
        'notesId': notesId
    }
    return render(request,'smartNotes/detailNotes.html', context)

def createNotes(request):
    form = CreateForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponse("Success")
        else:
            print ("NonSuccess")
            return HttpResponse("UnSuccess")
    else:
        context = {
            'form': form
        }
        return render(request, 'smartNotes/createNotes.html', context)
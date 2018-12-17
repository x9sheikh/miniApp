from django.shortcuts import render
from django.http import HttpResponse
from .models import Subject, MySmartNote, Mentor
from .forms import CreateForm
from django import forms
# Create your views here.
def index(request):
    context = {
        'myNotes': MySmartNote.objects.all()
    }
    return render(request,'smartNotes/index.html', context)

def detailNotes(request, notesId):
    class EditForm(forms.Form):
        title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your Title Here'}))
        subject = forms.CharField(label="Subject Name",
                                  widget=forms.TextInput(attrs={'placeholder': 'Enter your Subject Name'}))
        mentor = forms.CharField(label="Mentor Name",
                                 widget=forms.TextInput(attrs={'placeholder': 'Enter your Mentor Name'}))
        context = forms.CharField(
            label="Context",
            widget=forms.Textarea(
                attrs={
                    'placeholder': 'Write your Context, Here',
                    'rows': 10,
                    'cols': 80
                }
            ))
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
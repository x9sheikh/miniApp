from django.shortcuts import render
from django.http import HttpResponse
from .models import Subject, MySmartNote, Mentor
from .forms import CreateForm
from django import forms
from django.shortcuts import redirect
# Create your views here.
def index(request):
    context = {
        'myNotes': MySmartNote.objects.all()
    }
    return render(request,'smartNotes/index.html', context)

def detailNotes(request, notesId):

    class EditForm(forms.Form):
        ######################## GET DATA FROM DATA BASE #########################

        mySmartNotes = MySmartNote.objects.get(id=notesId)
        myTitle = mySmartNotes.title
        mySubject = mySmartNotes.subject
        myMentor = mySmartNotes.mentor
        myContext = mySmartNotes.context

        ######################## HERE, IS A EDIT FORM ###########################
        title = forms.CharField(initial=myTitle,
                                widget=forms.TextInput(attrs={'placeholder': 'Enter your Title Here'}))
        subject = forms.CharField(initial=mySubject,
                                  label="Subject Name",
                                  widget=forms.TextInput(attrs={'placeholder': 'Enter your Subject Name'}))
        mentor = forms.CharField(initial=myMentor,
                                 label="Mentor Name",
                                 widget=forms.TextInput(attrs={'placeholder': 'Enter your Mentor Name'}))
        context = forms.CharField(initial=myContext,
                                  label="Context",
                                  widget=forms.Textarea(
                                      attrs={
                                        'placeholder': 'Write your Context, Here',
                                        'rows': 10,
                                        'cols': 80
                                            }
                                                        )
                                  )
    form = EditForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            ##################### CREATE MY-SMART-NOTE OBJECT ################
            mySmartNote = MySmartNote.objects.get(id=notesId)

            ################## CREATE MENTOR OBJECT AND SET THE NEW NAME ##############
            mentor = Mentor.objects.get(id=mySmartNote.mentor.id)
            mentor.name = form.cleaned_data['mentor']
            mentor.save()

            ################## CREATE SUBJECT OBJECT AND SET THE NEW NAME ##############
            subject = Subject.objects.get(id=mySmartNote.subject.id)
            subject.name = form.cleaned_data['subject']
            subject.save()

            #################### SET TITLE AND CONTEXT TOO AND SAVE MY-SMART-NOTES#########################
            mySmartNote.title = form.cleaned_data['title']
            mySmartNote.context = form.cleaned_data['context']
            mySmartNote.save()


            return redirect('index')
        else:
            context = {
                'notesId': notesId,
                'error': 'Something going wrong'

            }
            return render(request, 'smartNotes/detailNotes.html', context)
    else:
        context = {
            'form': form,
            'notesId': notesId
        }
        return render(request, 'smartNotes/detailNotes.html', context)


def createNotes(request):
    form = CreateForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            ######################## DECLARE VARIABLES & INITIALIZED IT WITH INPUT FORMS #######
            title = form.cleaned_data['title']
            subject = form.cleaned_data['subject']
            mentor = form.cleaned_data['mentor']
            context = form.cleaned_data['context']
            ######################### CREATE MENTOR OBJECTS AND SAVE WITH THE NEW VALUE ########
            mentorObject = Mentor.objects.create(name=mentor)
            mentorObject.save()
            ######################### CREATE SUBJECT OBJECTS AND SAVE WITH THE NEW VALUE #######
            subjectObject = Subject.objects.create(name=subject)
            subjectObject.save()

            ######################### CREATE SMART-NOTE OBJECTS AND INTIALIZED IT'S ALL ATTRIBUTES
            mySmartNoteObject = MySmartNote.objects.create(
                title=title,
                subject=subjectObject,
                mentor=mentorObject,
                context=context
            )
            mySmartNoteObject.save()
            return redirect('index')
        else:
            context = {
                'form': form,
                'error': 'Something going wrong'
            }
            return render(request, 'smartNotes/createNotes.html', context)
    else:
        context = {
            'form': form
        }
        return render(request, 'smartNotes/createNotes.html', context)
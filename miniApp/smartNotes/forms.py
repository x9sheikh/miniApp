from django import forms
from .models import SmartNotes

class CreateForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter your Title Here'}))
    subjectName = forms.CharField(label="Subject Name")
    mentorName = forms.CharField(label="Mentor Name")
    notes = forms.CharField(
        label="Notes",
        widget= forms.Textarea(
            attrs={
                'palceholder': 'Write your Notes, Here',
                'rows': 10,
                'cols': 80
            }
        ))


    class Meta:
        model = SmartNotes
        fields = [
            'title',
            'subjectName',
            'mentorName',
            'notes'
        ]


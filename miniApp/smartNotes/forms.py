from django import forms
from .models import SmartNotes

class CreateForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter your Title Here'}))
    subject = forms.CharField(label="Subject Name")
    mentor = forms.CharField(label="Mentor Name")
    context = forms.CharField(
        label="Context",
        widget= forms.Textarea(
            attrs={
                'palceholder': 'Write your Notes Context, Here',
                'rows': 10,
                'cols': 80
            }
        ))


    class Meta:
        model = SmartNotes
        fields = [
            'title',
            'subject',
            'mentor',
            'context'
        ]


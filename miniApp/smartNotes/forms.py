from django import forms
from .models import MySmartNote

class CreateForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter your Title Here'}))
    subject = forms.CharField(label="Subject Name", widget= forms.TextInput(attrs={'placeholder':'Enter your Subject Name'}))
    mentor = forms.CharField(label="Mentor Name", widget=forms.TextInput(attrs={'placeholder': 'Enter your Mentor Name'}))
    context = forms.CharField(
        label="Context",
        widget= forms.Textarea(
            attrs={
                'placeholder': 'Write your Context, Here',
                'rows': 10,
                'cols': 80
            }
        ))

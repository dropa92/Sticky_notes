from django import forms
from .models import Note

# In this class we set up the form using ModelForm


class Note_form(forms.ModelForm):

    class Meta:
        model = Note
        fields = ['title', 'content']

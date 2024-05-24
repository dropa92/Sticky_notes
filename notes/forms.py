from django import forms
from .models import Note,Post,Author

# In this class we set up the form using ModelForm


class Note_form(forms.ModelForm):

    class Meta:
        model = Note
        fields = ['title', 'content']


class Post_form(forms.ModelForm):
    author_name = forms.CharField(max_length=255, required=False)  # Nuevo campo para el nombre del autor

    class Meta:
        model = Post
        fields = ['title', 'content', 'author_name']
    
    def save(self, commit=True):
        author_name = self.cleaned_data.pop('author_name')
        instance = super().save(commit=False)
        if author_name:
            author, created = Author.objects.get_or_create(name=author_name)
            instance.author = author
        if commit:
            instance.save()
        return instance
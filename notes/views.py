from django.shortcuts import render, get_object_or_404, redirect
from .models import Note
from .forms import Note_form


# We use this file to create our views

# This view get all the notes from the database
# it sends them all to note_list.html
def note_list(request):

    notes = Note.objects.all()

    notes_context = {
        'notes': notes,
        'page_title': 'List of Notes'
    }

    return render(request, 'note_list.html', notes_context)


# This view obtain a specific note from the database
# Then it sends it to note_detail.html
def note_detail(request, pk):

    note = get_object_or_404(Note, pk=pk)
    return render(request, 'note_detail.html', {'note': note})


# This view check if the request is POST and save a note in the database
# In other hand it renders to note_form.html
def note_create(request):

    if request.method == 'POST':
        form = Note_form(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.save()
            return redirect('note_list')
    else:
        form = Note_form()

    return render(request, 'note_form.html', {'form': form})


# This view check if the request is POST and save the modify note
# If the request is not POST render the note to be modified
def note_update(request, pk):
    note = get_object_or_404(Note, pk=pk)

    if request.method == 'POST':
        form = Note_form(request.POST, instance=note)
        if form.is_valid():
            note = form.save(commit=False)
            note.save()
            return redirect('note_list')
    else:
        form = Note_form(instance=note)

    return render(request, 'note_form.html', {'form': form})


# This view get the note and delete it from the database
def note_delete(request, pk):

    note = get_object_or_404(Note, pk=pk)
    note.delete()
    return redirect('note_list')

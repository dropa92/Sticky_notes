from django.shortcuts import render, get_object_or_404, redirect
from .models import Note, Post
from .forms import Note_form, Post_form


# We use this file to create our views

# This view get all the notes from the database
# it sends them all to note_list.html
def list(request):

    notes = Note.objects.all()
    posts = Post.objects.all()

    context = {
        'notes': notes,
        'page_title': 'List of Notes and Posts',
        'posts': posts,
    }

    return render(request, 'list.html', context)


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
            return redirect('list')
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
            return redirect('list')
    else:
        form = Note_form(instance=note)

    return render(request, 'note_form.html', {'form': form})


# This view get the note and delete it from the database
def note_delete(request, pk):

    note = get_object_or_404(Note, pk=pk)
    note.delete()
    return redirect('list')

# This view check if the request is POST and save a post in the database
# In other hand it renders to create_post.html
def create_post(request):
    if request.method == 'POST':
        form = Post_form(request.POST)
        if form.is_valid():
            form.author_name = request.POST['author_name']
            print('alojomora', form)
            post = form.save(commit=False)
            if request.user.is_authenticated:
              post.author = request.user
              print('Entra aquí')
            post.save()
            return redirect('list')
    else:
        form = Post_form()
    return render(request, 'create_post.html', {'form': form})


# This view obtain a specific post from the database
# Then it sends it to post_detail.html
def post_detail(request, pk):

    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})


def post_delete(request, pk):

    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('list')


# This view get the post and delete it from the database
def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = Post_form(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('list')
    else:
        form = Post_form(instance=post)

    return render(request, 'create_post.html', {'form': form})
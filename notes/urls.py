from django.urls import path
from .views import (list, note_detail, note_create, note_update,
                    note_delete, create_post, post_detail, post_delete,
                    post_update)

urlpatterns = [
    # URL pattern to display the list of notes and posts
    path('', list, name='list'),

    # URL pattern to display the content of a note
    path('note/<int:pk>/', note_detail, name='note_detail'),

    # URL pattern to create a new note
    path('note/new/', note_create, name='note_create'),

    # URL pattern to update the content of a note
    path('note/<int:pk>/edit/', note_update, name='note_update'),

    # URL pattern to delete a note
    path('note/<int:pk>/delete/', note_delete, name='note_delete'),
    
    # URL pattern to create a new post
    path('create/', create_post, name='create_post'),
    
    # URL pattern to display the content of a post
    path('post/<int:pk>/', post_detail, name='post_detail'),
    
    # URL pattern to delete a post
    path('post/<int:pk>/delete/', post_delete, name='post_delete'),
    
    # URL pattern to update the content of a post
    path('post/<int:pk>/edit/', post_update, name='post_update'),
]

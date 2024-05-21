from django.urls import path
from .views import (note_list, note_detail, note_create, note_update,
                    note_delete)

urlpatterns = [
    # URL pattern to display the list of notes
    path('', note_list, name='note_list'),

    # URL pattern to display the content of a note
    path('note/<int:pk>/', note_detail, name='note_detail'),

    # URL pattern to create a new note
    path('note/new/', note_create, name='note_create'),

    # URL pattern to update the content of a note
    path('note/<int:pk>/edit/', note_update, name='note_update'),

    # URL pattern to delete a note
    path('note/<int:pk>/delete/', note_delete, name='note_delete'),
]

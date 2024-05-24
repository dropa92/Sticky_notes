from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Post
from .models import Author
from .models import Note
 # Register your models here.
 
 # Note model
admin.site.register(Note)
 # Post model
admin.site.register(Post)
 # Author model
admin.site.register(Author)
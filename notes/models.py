from django.db import models


# We use this class to create our model here.
class Note(models.Model):

    title = models.CharField(max_length=255)
    content = models.TextField()


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey('Author', on_delete=models.CASCADE,
 null=True, blank=True)

class Author(models.Model):
    name = models.CharField(max_length=255)
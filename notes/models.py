from django.db import models


# We use this class to create our model here.
class Note(models.Model):

    title = models.CharField(max_length=255)
    content = models.TextField()

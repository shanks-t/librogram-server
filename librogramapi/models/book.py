from django.db import models
from librogramapi.models.tag import Tag

class Book(models.Model):

    title = models.CharField(max_length=60)
    author = models.CharField(max_length=60)
    description = models.TextField(max_length=160)
    num_of_pages = models.IntegerField()
    date_published = models.DateField()
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title
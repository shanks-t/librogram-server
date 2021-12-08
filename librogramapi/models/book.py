from django.db import models
from librogramapi.models.tag import Tag

class Book(models.Model):

    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=60)
    author = models.CharField(max_length=60)
    image_path = models.URLField()
    description = models.TextField()
    page_count = models.IntegerField()
    publisher = models.CharField(max_length=60)
    date_published = models.DateField()
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title
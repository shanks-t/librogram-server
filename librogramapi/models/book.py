from django.db import models
from django.contrib.auth.models import User
from librogramapi.models.tag import Tag

class Book(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=60)
    author = models.CharField(max_length=60)
    image_path = models.URLField()
    description = models.TextField()
    page_count = models.IntegerField()
    publisher = models.CharField(max_length=60)
    date_published = models.DateField()
    checkout_date = models.DateField(auto_now=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title
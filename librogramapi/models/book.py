from django.db import models
from django.contrib.auth.models import User
from django.db.models import constraints
from django.db.models.constraints import UniqueConstraint
from librogramapi.models.tag import Tag
from librogramapi.models.author import Author

class Book(models.Model):

    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=60)
    authors = models.ManyToManyField(Author)
    image_path = models.URLField(null=True)
    description = models.TextField(null=True)
    page_count = models.IntegerField(null=True)
    publisher = models.CharField(max_length=60, null=True)
    date_published = models.CharField(max_length=10)
    checkout_date = models.DateField(auto_now=True)
    tags = models.ManyToManyField(Tag)

    # @property
    # def readers_list(self):
    #     user_books = UserBook.objects.filter(book__title=self.title, book__author=self.author)
    #     readers = []
    #     for book in user_books:
    #         reader = book.user.username
    #         readers.append(reader)
        
    #     return readers


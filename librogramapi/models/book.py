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

    @property
    def readers_list(self):
        books = Book.objects.filter(title=self.title, author=self.author)
        readers = []
        for book in books:
            readers.append(book.user.username)
        
        return readers
from django.db import models
from django.contrib.auth.models import User
from django.db.models import constraints
from django.db.models.constraints import UniqueConstraint
from librogramapi.models.tag import Tag

class Book(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=60)
    author = models.CharField(max_length=60)
    image_path = models.URLField(null=True)
    description = models.TextField(null=True)
    page_count = models.IntegerField(null=True)
    publisher = models.CharField(max_length=60)
    date_published = models.CharField(max_length=10)
    checkout_date = models.DateField(auto_now=True)
    tags = models.ManyToManyField(Tag)

    @property
    def readers_list(self):
        books = Book.objects.filter(title=self.title, author=self.author)
        readers = []
        for book in books:
            reader = book.user.username
            readers.append(reader)
        
        return readers

    class Meta:
        db_table = 'Book'
        constraints = [
            models.UniqueConstraint(fields=['user', 'title', 'author'], name='unique_user_book')
        ]
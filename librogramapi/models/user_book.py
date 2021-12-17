from django.db import models
from django.contrib.auth.models import User
from librogramapi.models.status import Status
from librogramapi.models.tag import Tag
from librogramapi.models.book import Book

class UserBook(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey("Book", on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, default=1)
    rating = models.FloatField(null=True)
    review = models.TextField(null=True)
    start_date = models.DateField(null=True)
    finish_date = models.DateField(null=True)
    current_page = models.IntegerField(null=True)



from django.db import models
from django.contrib.auth.models import User


class UserBook(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey("Book", on_delete=models.CASCADE)
    status = models.ForeignKey('Status', on_delete=models.CASCADE)
    rating = models.FloatField()
    review = models.TextField()
    checkout_date = models.DateField(auto_now=True)
    start_date = models.DateField(blank=True)
    finish_date = models.DateField(null=True)
    current_page = models.IntegerField(blank=True)

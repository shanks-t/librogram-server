from django.db import models
from django.contrib.auth.models import User


class ReadingGoal(models.Model):

    number_of_pages = models.IntegerField(null=True)
    number_of_books = models.IntegerField(null=True)
    start_date = models.DateField(auto_now=True)
    end_date = models.DateField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)



from django.db import models
from django.contrib.auth.models import User

class ReaderBook(models.Model):
    reader = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey("Book", on_delete=models.CASCADE)
    rating = models.IntegerField()
    review = models.TextField()
    status = models.ForeignKey("Status", on_delete=models.CASCADE)
    checkout_date = models.DateField(auto_now=True)
    finish_date = models.DateField()
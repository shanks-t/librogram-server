from django.db import models
from django.contrib.auth.models import User

class Status(models.Model):
    status = models.CharField(max_length=50)
    reader = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey("Book", on_delete=models.CASCADE)
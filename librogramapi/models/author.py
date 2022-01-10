from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    name = models.TextField(max_length=100, default='none', null=True)


    def __str__(self):
        return self.name
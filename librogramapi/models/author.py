from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    author = models.TextField(max_length=100, default='none', null=True)



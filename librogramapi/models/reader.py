from django.db import models
from django.contrib.auth.models import User


class Reader(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=70)
    profile_image_url = models.URLField()
    subscriber = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
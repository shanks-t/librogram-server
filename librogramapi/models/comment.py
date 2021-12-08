from django.db import models
from django.contrib.auth.models import User


class Comment(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey("Book", on_delete=models.CASCADE, related_name="comments")
    created_on = models.DateField(auto_now=True)



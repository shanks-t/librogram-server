from django.db import models

class BookTag(models.Model):
    tag = models.ForeignKey("Tag", on_delete=models.CASCADE)
    book = models.ForeignKey("Book", on_delete=models.CASCADE)

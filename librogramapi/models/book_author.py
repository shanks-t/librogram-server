from django.db import models

class BookAuthor(models.Model):
    author = models.ForeignKey("Author", on_delete=models.CASCADE)
    book = models.ForeignKey("Book", on_delete=models.CASCADE)

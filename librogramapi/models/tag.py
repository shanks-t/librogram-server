from django.db import models

class Tag(models.Model):
    label = models.CharField(max_length=60)

    class Meta:
        db_table = 'Tag'
        constraints = [
            models.UniqueConstraint(fields=['label'], name='unique_tag')
        ]
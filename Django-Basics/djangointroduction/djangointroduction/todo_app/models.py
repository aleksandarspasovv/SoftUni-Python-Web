from django.db import models
from django.db.models import CharField


# Create your models here.
class Task(models.Model):
    name = models.CharField(
        max_length=50,
    )

    description = models.TextField()

    created_at = models.DateField(
        auto_now_add=True,
    )

    def __str__(self):
        return self.name
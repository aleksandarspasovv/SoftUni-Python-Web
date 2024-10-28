from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from profiles.choices import GenreChoices


# Create your models here.
class Profile(models.Model):
    username = models.CharField(
        max_length=15,
        validators=[
            MinLengthValidator(2),
        ],

    )

    email = models.EmailField()

    age = models.PositiveIntegerField(
        blank=True,
        null=True,
    )



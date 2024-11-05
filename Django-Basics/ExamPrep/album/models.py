from django.core.validators import MinValueValidator
from django.db import models

from profiles.choices import GenreChoices
from profiles.models import Profile


# Create your models here.
class Album(models.Model):
    album_name = models.CharField(
        unique=True,
        max_length=30,
    )

    artist = models.CharField(
        max_length=30,
        choices=models.TextChoices(GenreChoices),
    )

    description = models.TextField()

    image_url = models.URLField()

    price = models.FloatField(
        validators=[MinValueValidator(0.0)],
    )

    owner = models.ForeignKey(
        to=Profile,

    )
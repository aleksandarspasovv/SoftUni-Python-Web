from django.db import models


class GenreChoices(models.TextChoices):
    POP_MUSIC = 'Pop Music', 'Pop Music'
    JAZZ_MUSIC = 'Jazz Music', 'Jazz Music'

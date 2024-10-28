from django.core.exceptions import ValidationError
from django.db import models


def validate_letters_only(value):
    if not value.isalpha():
        raise ValidationError("Your name must contain letters only!")

class Author(models.Model):
    first_name = models.CharField(
        max_length=40,
        validators=[
            validate_letters_only
        ])

    last_name = models.CharField(
        max_length=50,
        validators=[
            validate_letters_only
        ])

    passcode = models.CharField(
        max_length=6,
    )

    pets_number = models.PositiveSmallIntegerField()

    info = models.TextField(
        blank=True,
        null=True,
    )

    image_url = models.URLField(
        blank=True,
        null=True,
    )

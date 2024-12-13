from django.db import models
from django.core.exceptions import ValidationError


def validate_nickname(value):
    if not value.isalnum():
        raise ValidationError("Your nickname is invalid!")


class Traveler(models.Model):
    nickname = models.CharField(
        max_length=30,
        unique=True,
        validators=[validate_nickname]
    )

    email = models.EmailField(
        max_length=30,
        unique=True
    )

    country = models.CharField(max_length=3)

    about_me = models.TextField(
        blank=True,
        null=True
    )

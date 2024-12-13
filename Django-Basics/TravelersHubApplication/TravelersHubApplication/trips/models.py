from django.db import models
from TravelersHubApplication.travelers.models import Traveler


class Trip(models.Model):
    destination = models.CharField(max_length=100)

    summary = models.TextField()

    start_date = models.DateField()

    duration = models.PositiveSmallIntegerField(default=1)

    image_url = models.URLField(
        blank=True,
        null=True
    )

    traveler = models.ForeignKey(
        Traveler,
        on_delete=models.CASCADE
    )


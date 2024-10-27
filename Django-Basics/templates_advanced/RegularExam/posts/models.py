# posts/models.py
from django.db import models

from author.models import Author


class Post(models.Model):
    title = models.CharField(max_length=50, unique=True)
    image_url = models.URLField()
    content = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)  # Ensure this references Author correctly

    def __str__(self):
        return self.title

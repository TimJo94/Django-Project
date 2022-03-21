from django.db import models


class Post(models.Model):
    author = models.CharField(max_length=55)
    title = models.CharField(max_length=85)
    slug = models.SlugField(max_length=55)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    text = models.TextField()

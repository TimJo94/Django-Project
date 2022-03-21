from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

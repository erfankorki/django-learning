from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255)
    summary = models.TextField(default="")
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=255)

from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Page(models.Model):
    slug = models.CharField(unique=True, max_length=100)
    url_title = models.CharField(max_length=20)
    title = models.CharField(max_length=100)
    body = models.TextField()
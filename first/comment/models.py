from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from article.models import Article


class Comments(models.Model):
    body = models.TextField()
    author = models.ForeignKey(User)
    date = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Article)
    publish = models.BooleanField(default=False)

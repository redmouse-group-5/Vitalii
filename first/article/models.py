from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Article(models.Model):

    title = models.CharField(max_length=100)
    author = models.ForeignKey(User)
    body = models.TextField()
    date_create=models.DateTimeField(auto_now_add=True)
    date_update=models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="article_image", blank=True, null=True, default=None)
    publish = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_comment(self):
        from comment.models import Comments
        comments = Comments.objects.filter(article=self.id, publish=True).count()
        return comments
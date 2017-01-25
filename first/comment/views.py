from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.urls import reverse
from django.views import View

from article.models import Article
from comment.forms import CommentForm
from comment.models import Comments


class CommentViews(View):
    def get(self, request, id):
        return redirect(reverse('index_page'))

    def post(self, request, id):
        form = CommentForm(request.POST)
        if form.is_valid():
            article = get_object_or_404(Article, id=id)
            comment = Comments(
                body=request.POST['body'],
                article=article,
                author=request.user
            )
            comment.save()
        return redirect(request.META['HTTP_REFERER'])

# def comment_add(request, id):
#     form = CommentForm(request.POST)
#     if request.method =='POST' and form.is_valid():
#         article = get_object_or_404(Article, id=id)
#         comment = Comments(
#             body=request.POST['body'],
#             article=article,
#             author=request.user
#         )
#         comment.save()
#     else:
#         raise Http404
#     return redirect(request.META['HTTP_REFERER'])
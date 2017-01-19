from django.shortcuts import render, render_to_response, redirect, get_object_or_404

# Create your views here.
from django.http import HttpResponse, JsonResponse
import datetime

from article.models import Article


def current_datetime(request, year=datetime.datetime.now().year):
    now = datetime.datetime.now()
    html = "<html><body><h1>It is now %s.</h1></body></html>" % now
    if request.method == "GET":
        html = "<html><body><h1>It is now %s.</h1> %s </body></html>" % (now, year)
    return HttpResponse(html)


def get_index(request):
    articles = Article.objects.filter(publish=True)
    # return render(request, 'index.html', {'nowwwww': now})
    return render_to_response('index.html', locals())

def get_article(request, id):
    article = get_object_or_404(Article, id=id, publish=True)
    return render_to_response('article/article.html', {'article': article})

def google(request):
    return redirect('http://google.kg')
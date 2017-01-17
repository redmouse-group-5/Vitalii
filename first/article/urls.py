from django.conf.urls import url
from article.views import current_datetime, get_article

urlpatterns = [
    url(r'^$', current_datetime),
    url(r'^(?P<id>[0-9]+)/$', get_article, name='article'),
    url(r'^(?P<year>[0-9]{4})/$', current_datetime, name='article_year'),

]

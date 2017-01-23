"""first URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from article.views import current_datetime, get_index, google
from django.conf import settings
from django.conf.urls.static import static

from comment.views import comment_add
from page.views import get_page

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', get_index, name='index_page'),
    url(r'^google/$', google),
    url(r'^current_datatime/$', current_datetime),
    url(r'^articles/', include('article.urls', namespace="article")),
    url(r'^artic/', include('article.urls', namespace="artic")),
    url(r'^comments_add/(?P<id>\d+)/$', comment_add, name="comment_add"),
    url(r'^page/(?P<slug>\S+)/$', get_page, name="page")

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
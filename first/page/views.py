from django.shortcuts import render, get_object_or_404


def get_page(request, slug):
    from page.models import Page
    inner_page = get_object_or_404(Page, slug=slug)
    return render(request, 'page/about.html', locals())
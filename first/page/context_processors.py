def get_page_url(request):
    from page.models import Page
    return {'page': Page.objects.all()}

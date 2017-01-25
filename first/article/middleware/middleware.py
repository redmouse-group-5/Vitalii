from django.utils.deprecation import MiddlewareMixin

from django.conf import settings


class SimpleMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if not hasattr(request, 'city'):
            request.city = settings.DEFAULT_CITY
        return None
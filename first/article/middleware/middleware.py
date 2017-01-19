from django.utils.deprecation import MiddlewareMixin

class SimpleMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if not hasattr(request, 'city'):
            request.city = "Bishkek"
        return None
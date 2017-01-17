from django.utils.deprecation import MiddlewareMixin

class SimpleMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if 'city' not in request:
            request.city = "Bishkek"
        return None
from django.core.exceptions import PermissionDenied


class ExampleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request, *args, **kwargs):
        print('middleware called')
        response = self.get_response(request)
        user_agent = request.META.get('HTTP_USER_AGENT')
        print("##################")
        print(user_agent)
        print("##################")
        # if user_agent:
        #     raise PermissionDenied("Vayena")

        print(request.META.get('HTTP_X_FORWARDED_FOR'))

        ip_address = self.get_client_ip(request)
        print("##################")
        print(f"IP Address: {ip_address}")
        print("##################")
        if ip_address != '127.0.0.1':
            raise PermissionDenied("This ip address is not allowed")
             

        return response
    
    def get_client_ip(self, request):
            """Utility method to get the client's IP address"""
            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            if x_forwarded_for:
                ip = x_forwarded_for.split(',')[0]
            else:
                ip = request.META.get('REMOTE_ADDR')
            return ip

    # def process_exception(self, request, exception):
    #     print(f"Exception handled: {exception}")
    #     from django.http import JsonResponse
    #     response_data = {
    #         'error': str(exception)
    #     }
    #     return JsonResponse(response_data, status=400)


class OrganizationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request, *args, **kwargs):
        response = self.get_response
        breakpoint()
        return response




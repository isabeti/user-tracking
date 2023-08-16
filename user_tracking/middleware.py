import datetime
from config import settings
from .models import UserTracking

class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        is_ignore_tracking = False
        for i in settings.URL_IGNORE_TRACKING:
            if i in request.path:
                is_ignore_tracking = True
                break
        if is_ignore_tracking == False:
            create_obj = UserTracking.objects.create(user=request.user if request.user.is_authenticated else None, url=request.path)
        
        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response
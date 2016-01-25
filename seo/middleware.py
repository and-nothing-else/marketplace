from django.conf import settings
from django.http import Http404
from .views import seo_file


class SEOFileMiddleware(object):
    @staticmethod
    def process_response(request, response):
        if response.status_code != 404:
            return response  # No need to check for a seo file for non-404 responses.
        try:
            return seo_file(request, request.path_info)
        # Return the original response if any errors happened. Because this
        # is a middleware, we can't assume the errors will be caught elsewhere.
        except Http404:
            return response
        except:
            if settings.DEBUG:
                raise
            return response

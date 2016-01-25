from django.shortcuts import get_object_or_404
from django.http import Http404, HttpResponse
from .models import *


def seo_file(request, url):
    if not url.startswith('/'):
        url = '/' + url
    try:
        f = get_object_or_404(SEOFile, path__exact=url)
    except Http404:
        raise
    return HttpResponse(f.content, content_type=f.content_type)

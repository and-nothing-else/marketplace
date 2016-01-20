"""marketplace URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^admin_tools/', include('admin_tools.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^accounts/', include('user.urls', namespace='user')),
    url(r'^feedback/', include('feedback.urls', namespace='feedback')),
    url(r'^help/', include('help.urls', namespace='help')),
    url(r'^tariff/', include('tariff.urls', namespace='tariff')),
    url(r'^order/', include('order.urls', namespace='order')),
    url(r'^geoip/', include('django_geoip.urls')),
    url(r'^shops/', include('shops.urls', namespace='shops')),
    url(r'^search/', include('search.urls', namespace='search')),
    url(r'^articles/', include('articles.urls', namespace='articles')),
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
    url(r'^', include('catalog.urls', namespace='catalog')),
]


if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    ]

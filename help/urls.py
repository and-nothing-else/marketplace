from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', HelpListView.as_view(), name='list'),
    url(r'^(?P<slug>.+)/$', HelpDetailView.as_view(), name='detail'),
]

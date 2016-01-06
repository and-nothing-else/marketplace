from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', ShopListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', ShopDetailView.as_view(), name='detail'),
]

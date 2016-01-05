from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^set_tariff/(?P<tariff_id>\d+)/$', set_tariff, name='set_tariff'),
]

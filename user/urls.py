from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^profile/$', ShopUpdateView.as_view(), name='shop_update'),
    url(r'^tariff/$', TariffList.as_view(), name='tariff_list'),
]

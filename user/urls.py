from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^profile/$', ShopUpdateView.as_view(), name='shop_update'),
    url(r'^tariff/$', TariffList.as_view(), name='tariff_list'),
    url(r'^items/$', UserItemListView.as_view(), name='item_list'),
    url(r'^items/add/$', UserItemSelectCategoryView.as_view(), name='item_create'),
    url(r'^items/add2category/(?P<category_id>\d+)/$', UserItemCreateView.as_view(), name='item_create_step2'),
    url(r'^items/add_sku4item/(?P<item_id>\d+)/$', UserItemSKUCreateView.as_view(), name='item_create_sku'),
    url(r'^items/(?P<pk>\d+)/$', UserItemUpdateView.as_view(), name='item_update'),
]

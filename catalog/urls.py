from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^(?P<slug>[\w-]+)/$', CatalogCategoryView.as_view(), name='category_detail'),
    url(r'^(?P<category_slug>[\w-]+)/(?P<pk>\d+)/$', ItemDetailView.as_view(), name='item_detail'),
]

from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', CatalogSearchView.as_view(), name='catalog_search'),
]

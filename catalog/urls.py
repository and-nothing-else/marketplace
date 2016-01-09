from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^(?P<slug>.+)/$', CatalogCategoryView.as_view(), name='category_detail'),
]

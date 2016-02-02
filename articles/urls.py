from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', ArticleListView.as_view(), name='article_list'),
    url(r'^(?P<slug>.+)/$', ArticleDetailView.as_view(), name='article_detail'),
]

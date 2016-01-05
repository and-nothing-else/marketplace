from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', OrderFormView.as_view(), name='order_form'),
    url(r'^go_pay/$', GoPayView.as_view(), name='go_pay'),
]

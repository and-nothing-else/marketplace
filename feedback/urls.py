from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', TicketListView.as_view(), name='ticket_list'),
    url(r'^(?P<pk>\d+)/$', TicketDetailView.as_view(), name='ticket_detail'),
    url(r'^new/$', TicketCreateView.as_view(), name='ticket_create'),
]

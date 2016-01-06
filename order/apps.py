from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class OrderConfig(AppConfig):
    name = 'order'
    verbose_name = _('Orders')

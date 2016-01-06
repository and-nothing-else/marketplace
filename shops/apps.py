from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class ShopsConfig(AppConfig):
    name = 'shops'
    verbose_name = _('Shops')

from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class TariffConfig(AppConfig):
    name = 'tariff'
    verbose_name = _('Tariff control')

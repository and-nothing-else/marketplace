from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class ProfileConfig(AppConfig):
    name = 'profile'
    verbose_name = _('User profiles')

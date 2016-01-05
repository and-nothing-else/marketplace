from django.apps import AppConfig
from django.utils.translation import pgettext_lazy


class DictionaryConfig(AppConfig):
    name = 'dictionary'
    verbose_name = pgettext_lazy('App name', 'Dictionaries')

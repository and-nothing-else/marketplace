from django.db import models
from django.utils.translation import ugettext_lazy as _


class Tariff(models.Model):
    name = models.CharField(_('name'), max_length=32)
    goods = models.PositiveSmallIntegerField(_('goods count'))
    price = models.PositiveSmallIntegerField(_('price'), help_text=_('roubles per month'))
    ordering = models.IntegerField(_('ordering'), default=10)
    is_recommended = models.BooleanField(_('is recommended'), default=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['ordering']
        verbose_name = _('tariff')
        verbose_name_plural = _('tariffs')

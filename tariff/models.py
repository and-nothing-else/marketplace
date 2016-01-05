from django.db import models
from django.utils.translation import ugettext_lazy as _


class TariffManager(models.Manager):

    def get_default(self):
        try:
            return self.get_queryset().filter(is_default=True).first()
        except self.get_queryset().DoesNotExist:
            return None


class Tariff(models.Model):
    name = models.CharField(_('name'), max_length=32)
    goods = models.PositiveSmallIntegerField(_('goods count'))
    price = models.FloatField(_('price'), help_text=_('roubles per day'))
    ordering = models.IntegerField(_('ordering'), default=10)
    is_recommended = models.BooleanField(_('is recommended'), default=False)
    is_default = models.BooleanField(_('default'), default=False)

    objects = TariffManager()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['ordering']
        verbose_name = _('tariff')
        verbose_name_plural = _('tariffs')

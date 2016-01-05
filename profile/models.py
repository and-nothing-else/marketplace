from django.db import models
from django.utils.translation import ugettext_lazy as _


class Shop(models.Model):
    owner = models.ForeignKey('user.MarketplaceUser', verbose_name=_('owner'))
    name = models.CharField(_('shop name'), max_length=512)
    address = models.CharField(_('address'), max_length=512)
    phone = models.CharField(_('phone'), max_length=128)
    region = models.ForeignKey('dictionary.Region', verbose_name=_('region'), blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = _('shop')
        verbose_name_plural = _('shops')

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse_lazy
from ckeditor.fields import RichTextField


class ShopManager(models.Manager):
    def active(self):
        return self.get_queryset().filter(active=True)


class Shop(models.Model):
    owner = models.ForeignKey('user.MarketplaceUser', verbose_name=_('owner'))
    name = models.CharField(_('shop name'), max_length=512)
    address = models.CharField(_('address'), max_length=512)
    phone = models.CharField(_('phone'), max_length=128)
    region = models.ForeignKey('dictionary.Region', verbose_name=_('region'), blank=True, null=True)
    description = RichTextField(_('description'), blank=True, config_name='minimal')

    active = models.BooleanField(_('active'), default=True)

    objects = ShopManager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('shops:detail', args=[str(self.pk)])

    class Meta:
        ordering = ['name']
        verbose_name = _('shop')
        verbose_name_plural = _('shops')

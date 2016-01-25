from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse_lazy
from ckeditor.fields import RichTextField
from addresspicker.fields import AddressPickerField
from seo.models import SEOFieldsMixin


class ShopManager(models.Manager):
    def active(self):
        return self.get_queryset().filter(active=True)


class Shop(SEOFieldsMixin, models.Model):
    owner = models.OneToOneField('user.MarketplaceUser', verbose_name=_('owner'))
    name = models.CharField(_('shop name'), max_length=512)
    slug = models.SlugField(_('slug'), unique=True, help_text=_('used for create url'))
    address = models.CharField(_('address'), max_length=512)
    map_point = AddressPickerField(_('on map'), blank=True, null=True)
    phone = models.CharField(_('phone'), max_length=128)
    region = models.ForeignKey('dictionary.Region', verbose_name=_('region'), blank=True, null=True)
    description = RichTextField(_('description'), blank=True, config_name='minimal')

    active = models.BooleanField(_('active'), default=True)

    objects = ShopManager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('shops:detail', args=[str(self.slug)])

    def get_browser_title(self):
        return self.browser_title or self.name

    def get_meta_description(self):
        return self.meta_description or self.description

    class Meta:
        ordering = ['name']
        verbose_name = _('shop')
        verbose_name_plural = _('shops')

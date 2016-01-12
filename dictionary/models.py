from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_geoip.models import GeoLocationFacade, Region as GeoIPRegion


class Region(GeoLocationFacade):
    name = models.CharField(_('name'), max_length=256)
    is_default = models.BooleanField(default=False)
    region = models.ManyToManyField(GeoIPRegion, verbose_name=_('region contains'), blank=True, related_name='location')

    @classmethod
    def get_by_ip_range(cls, ip_range):
        if ip_range:
            return ip_range.region
        else:
            return cls.get_default_location()

    @classmethod
    def get_default_location(cls):
        try:
            return cls.objects.filter(is_default=True).first()
        except cls.DoesNotExist:
            return None

    @classmethod
    def get_available_locations(cls):
        return cls.objects.all()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('region')
        verbose_name_plural = _('regions')
        ordering = ['-is_default', 'name']


class Color(models.Model):
    name = models.CharField(_('name'), max_length=64)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('color')
        verbose_name_plural = _('colors')
        ordering = ['name']

from django.db import models
from django.utils.translation import ugettext_lazy as _


class SEOFieldsMixin(models.Model):
    browser_title = models.CharField(_('browser title'), max_length=512, null=True, blank=True)
    meta_description = models.TextField(_('meta description'), max_length=512, null=True, blank=True)

    class Meta:
        abstract = True

    def get_browser_title(self):
        return self.browser_title

    def get_meta_description(self):
        return self.meta_description


class SEOFile(models.Model):
    description = models.CharField(_('description'), max_length=256, null=True, blank=True,
                                   help_text=_('e.g. Yandex-validator'))
    path = models.CharField(_("path"), max_length=128, help_text=_("relative to site root. E.g. /123456789.html"))
    content_type = models.CharField('content_type', max_length=128, default='text/plain')
    content = models.TextField(_('content'), blank=True)

    def __str__(self):
        return self.description or self.path

    class Meta:
        ordering = ['path']
        verbose_name = _('SEO file')
        verbose_name_plural = _('SEO files')

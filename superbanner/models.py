from django.db import models
from django.utils.translation import ugettext_lazy as _
from sorl.thumbnail.fields import ImageField
from ckeditor.fields import RichTextField


class SuperBanner(models.Model):
    image = ImageField(_('image'), upload_to='superbanner')
    title = models.CharField(_('title'), max_length=64, null=True, blank=True)
    text = RichTextField(_('text'), blank=True)
    button_link = models.CharField(_('button link'), max_length=256, null=True, blank=True)
    button_label = models.CharField(_('button label'), max_length=32, null=True, blank=True)
    ordering = models.IntegerField(_('ordering'), default=100)

    def __str__(self):
        return self.title or self.image.url

    class Meta:
        ordering = ['ordering']
        verbose_name = _('superbanner')
        verbose_name_plural = _('superbanners')

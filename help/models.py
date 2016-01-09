from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse_lazy
from ckeditor.fields import RichTextField


class Help(models.Model):
    title = models.CharField(_('title'), max_length=512)
    text = RichTextField(_('text'))
    slug = models.SlugField(_('slug'), unique=True)
    ordering = models.IntegerField(_('ordering'), default=100)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy('help:detail', args=[str(self.slug)])

    class Meta:
        ordering = ['ordering']
        verbose_name = _('help article')
        verbose_name_plural = _('help')

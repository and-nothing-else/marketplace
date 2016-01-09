from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse_lazy
from treebeard.mp_tree import MP_Node


class Category(MP_Node):
    name = models.CharField(_('name'), max_length=64)
    slug = models.SlugField(_('slug'), unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('catalog:category_detail', args=[str(self.slug)])

    class Meta:
        verbose_name = _('catalog section')
        verbose_name_plural = _('catalog sections')

from django.db import models
from django.utils.translation import pgettext_lazy, ugettext_lazy as _
from django.core.urlresolvers import reverse_lazy
from treebeard.mp_tree import MP_Node
from ckeditor.fields import RichTextField
from sorl.thumbnail.fields import ImageField


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


class Item(models.Model):
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    category = models.ForeignKey(Category, verbose_name=_('category'))
    shop = models.ForeignKey('shops.Shop', verbose_name=_('shop'))
    active = models.BooleanField(_('active'), default=True)
    name = models.CharField(_('name'), max_length=256)
    article = models.CharField(pgettext_lazy('catalog item article', 'article'), max_length=16)
    price = models.PositiveIntegerField(_('price'))
    description = RichTextField(_('description'), blank=True, config_name='minimal')

    def __str__(self):
        return self.name

    def get_image(self):
        try:
            return self.itemphoto_set.first().photo
        except ItemPhoto.DoesNotExist:
            return None

    class Meta:
        ordering = ['-created_at']
        verbose_name = _('catalog item')
        verbose_name_plural = _('catalog items')


class ItemPhoto(models.Model):
    item = models.ForeignKey(Item, verbose_name=_('catalog item'))
    photo = ImageField(_('image'), upload_to='catalog')
    ordering = models.IntegerField(_('ordering'), default=100)

    def __str__(self):
        return self.photo.url

    class Meta:
        ordering = ['ordering']
        verbose_name = _('photo')
        verbose_name_plural = _('photos')

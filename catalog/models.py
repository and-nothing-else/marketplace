from django.db import models
from django.utils.translation import pgettext_lazy, ugettext_lazy as _
from django.core.urlresolvers import reverse_lazy
from treebeard.mp_tree import MP_Node
from ckeditor.fields import RichTextField
from sorl.thumbnail import get_thumbnail
from sorl.thumbnail.fields import ImageField
import json


class Category(MP_Node):
    name = models.CharField(_('name'), max_length=64)
    slug = models.SlugField(_('slug'), unique=True)
    sku_allowed = models.BooleanField(_('sku allowed'), default=True)
    size_set = models.ForeignKey('dictionary.SizeSet', verbose_name=_('size set'), blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('catalog:category_detail', args=[str(self.slug)])

    def get_size_set(self):
        if self.size_set:
            return self.size_set
        else:
            try:
                return self.get_parent().get_size_set()
            except AttributeError:
                return None

    def get_sizes(self):
        size_set = self.get_size_set()
        if size_set:
            return size_set.size_set.all()
        else:
            return None

    class Meta:
        verbose_name = _('catalog section')
        verbose_name_plural = _('catalog sections')


class ItemManager(models.Manager):
    def active(self):
        return self.get_queryset().filter(active=True)

    def active_for_location(self, location):
        return self.active().filter(shop__region__id=location.id)


class Item(models.Model):
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('updated at'), auto_now=True)
    category = models.ForeignKey(Category, verbose_name=_('category'))
    shop = models.ForeignKey('shops.Shop', verbose_name=_('shop'))

    active = models.BooleanField(_('active'), default=True)
    name = models.CharField(pgettext_lazy('item name', 'name'), max_length=256)
    article = models.CharField(pgettext_lazy('catalog item article', 'article'), max_length=16)
    price = models.PositiveIntegerField(_('price'))
    old_price = models.PositiveIntegerField(_('old price'), blank=True, null=True)

    description = RichTextField(_('description'), blank=True, config_name='minimal')
    color = models.ForeignKey('dictionary.Color', verbose_name=_('color'), blank=True, null=True)
    size = models.CharField(_('vendor size'), max_length=16, blank=True, null=True)
    standard_size = models.ForeignKey('dictionary.Size', verbose_name=_('standard size'), blank=True, null=True)
    fabric = models.CharField(_('fabric structure'), max_length=1024, blank=True, null=True)

    objects = ItemManager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('catalog:item_detail', args=[self.category.slug, self.pk])

    def get_edit_url(self):
        return reverse_lazy('user:item_update', args=[self.pk])

    def get_image(self):
        try:
            return self.itemphoto_set.first().photo
        except (ItemPhoto.DoesNotExist, AttributeError):
            try:
                return self.itemsku_set.first().itemskuphoto_set.first().photo
            except:
                return None

    def get_more_photos(self):
        return [photo.photo for photo in self.itemphoto_set.all()][1:]

    def get_sku_data(self):
        sku_list = {}
        for sku in self.itemsku_set.active():
            sku_list[sku.id] = {
                'sku_id': sku.id,
                'name': sku.color.name,
                'photos': [{
                    'preview': photo.get_thumbnail().url,
                    'large': photo.photo.url
                           } for photo in sku.itemskuphoto_set.all()],
                'sizes': [{
                    'vendor': size.size,
                    'standard': size.standard_size.value,
                    'description': size.standard_size.description,
                } for size in sku.itemskusize_set.all()]
            }
        return json.dumps(sku_list)

    def get_colors(self):
        return self.itemsku_set.active()

    def get_color(self):
        try:
            return self.color or self.get_colors().first().color.name
        except AttributeError:
            return None

    def get_sizes(self):
        output = []

        def in_output(s):
            for r in output:
                if r.size == s.size:
                    return True
            return False

        for item_size in ItemSKUSize.objects.filter(sku__item=self).order_by('standard_size__value'):
            if not in_output(item_size):
                output.append(item_size)
        return output

    def save(self, *args, **kwargs):
        user_items = self.shop.item_set.active()
        if self.pk:
            user_items = user_items.exclude(pk=self.pk)
        if user_items.count() >= self.shop.owner.tariff.goods:
            self.active = False
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-updated_at']
        verbose_name = _('catalog item')
        verbose_name_plural = _('catalog items')


class Photo(models.Model):
    photo = ImageField(_('image'), upload_to='catalog')
    ordering = models.IntegerField(_('ordering'), default=100)

    def __str__(self):
        return self.photo.url

    def get_thumbnail(self, size='150x150'):
        return get_thumbnail(self.photo, size, crop='center', quality=81)

    class Meta:
        abstract = True
        ordering = ['ordering', 'id']
        verbose_name = _('photo')
        verbose_name_plural = _('photos')


class ItemPhoto(Photo):
    item = models.ForeignKey(Item, verbose_name=_('catalog item'))


class ItemCustomProperty(models.Model):
    item = models.ForeignKey(Item, verbose_name=_('catalog item'))
    name = models.CharField(_('property name'), max_length=64)
    value = models.CharField(_('property value'), max_length=2048)
    ordering = models.IntegerField(_('ordering'), default=100)

    def __str__(self):
        return "{}: {}".format(self.name, self.value)

    class Meta:
        ordering = ['ordering']
        verbose_name = _('property')
        verbose_name_plural = _('properties')


class ItemSKUManager(models.Manager):
    def active(self):
        return self.get_queryset().filter(active=True)


class ItemSKU(models.Model):
    item = models.ForeignKey(Item, verbose_name=_('catalog item'))
    color = models.ForeignKey('dictionary.Color', verbose_name=_('color'))
    active = models.BooleanField(_('active'), default=True)

    objects = ItemSKUManager()

    def __str__(self):
        return "{name} ({color_label}: {color_value}, {size_label}: {size_value})".format(
            name=self.item.name,
            color_label=_('color'),
            color_value=self.color,
            size_label=_('sizes'),
            size_value=', '.join([size.size for size in self.itemskusize_set.all()])
        )

    def get_preview(self):
        return self.itemskuphoto_set.first().get_thumbnail('80x80')

    class Meta:
        ordering = ['color']
        verbose_name = 'SKU'


class ItemSKUSize(models.Model):
    sku = models.ForeignKey(ItemSKU)
    size = models.CharField(_('vendor size'), max_length=16)
    standard_size = models.ForeignKey('dictionary.Size', verbose_name=_('standard size'))

    def __str__(self):
        return self.size

    class Meta:
        ordering = ['size']
        verbose_name = _('SKU size')


class ItemSKUPhoto(Photo):
    sku = models.ForeignKey(ItemSKU)

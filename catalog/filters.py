import django_filters
from django.utils.translation import ugettext_lazy as _
from django.forms.widgets import CheckboxSelectMultiple
from .models import Item, ItemSKU


class ItemFilter(django_filters.FilterSet):

    class SizeFilter(django_filters.Filter):
        def __init__(self, *args, **kwargs):
            kwargs.update({
                'label': _('Size'),
                'widget': CheckboxSelectMultiple,
            })
            super().__init__(*args, **kwargs)

        def filter(self, qs, value):
            if value:
                sku_allowed = True  # TODO: ну понятно в общем
                if sku_allowed:
                    return qs.filter(itemsku__itemskusize__standard_size__value__in=value).distinct()
                else:
                    return qs.filter(standard_size=value)
            else:
                return qs

    class FabricFilter(django_filters.Filter):
        def __init__(self, *args, **kwargs):
            kwargs.update({
                'label': _('fabric structure'),
                'widget': CheckboxSelectMultiple,
            })
            super().__init__(*args, **kwargs)

        def filter(self, qs, value):
            if value:
                return qs.filter(fabric__in=value)
            else:
                return qs

    class ColorFilter(django_filters.Filter):
        def __init__(self, *args, **kwargs):
            kwargs.update({
                'label': _('color'),
                'widget': CheckboxSelectMultiple,
            })
            super().__init__(*args, **kwargs)

        def filter(self, qs, value):
            if value:
                sku_allowed = True
                if sku_allowed:
                    return qs.filter(itemsku__color__name__in=value).distinct()
                else:
                    return qs.filter(color__name__in=value)
            else:
                return qs

    price = django_filters.RangeFilter()
    size = SizeFilter()
    fabric = FabricFilter()
    color = ColorFilter()

    def __init__(self, data=None, queryset=None, prefix=None, strict=None, category=None):
        super().__init__(data, queryset, prefix, strict)
        if category:
            sizes = category.get_sizes()
            if sizes:
                self.filters['size'].field.choices = [
                    (size['value'], size['value'])
                    for size in category.get_sizes().values('value').distinct()
                    ]
            else:
                del self.filters['size']

            fabric_choices = [
                (item['fabric'], item['fabric'])
                for item in category.item_set.active().values('fabric').order_by('fabric').distinct()
                if item['fabric']
                ]
            if fabric_choices:
                self.filters['fabric'].field.choices = fabric_choices
            else:
                del self.filters['fabric']

            color_choices = [
                (item['color__name'], item['color__name'])
                for item in ItemSKU.objects.filter(
                        item__category=category, item__active=True
                ).values('color__name').order_by('color__name').distinct()
                ]
            if color_choices:
                self.filters['color'].field.choices = color_choices
            else:
                del self.filters['color']

    class Meta:
        model = Item
        fields = ['price']
        order_by = ['-updated_at', 'updated_at', 'price', '-price']

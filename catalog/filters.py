import django_filters
from django.utils.translation import ugettext_lazy as _
from django.forms.widgets import CheckboxSelectMultiple
from .models import Item


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
                sku_allowed = True
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

    price = django_filters.RangeFilter()
    size = SizeFilter()
    fabric = FabricFilter()

    def __init__(self, data=None, queryset=None, prefix=None, strict=None, category=None):
        super().__init__(data, queryset, prefix, strict)
        if category:
            self.filters['size'].field.choices = [
                (size['value'], size['value'])
                for size in category.size_set.size_set.values('value').distinct()
                ]
            self.filters['fabric'].field.choices = [
                (item['fabric'], item['fabric'])
                for item in category.item_set.active().values('fabric').order_by('fabric').distinct()
                ]
            pass

    class Meta:
        model = Item
        fields = ['price']
        order_by = ['-updated_at', 'updated_at', 'price', '-price']

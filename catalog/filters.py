import django_filters
from django.utils.translation import ugettext_lazy as _
from django.db.models import Q
from django.forms.widgets import CheckboxSelectMultiple
from .models import Item
from dictionary.models import Size


class ItemFilter(django_filters.FilterSet):

    class SizeFilter(django_filters.ModelMultipleChoiceFilter):
        def filter(self, qs, value):
            if value:
                sku_allowed = True
                if sku_allowed:
                    return qs.filter(itemsku__itemskusize__standard_size__in=value).distinct()
                else:
                    return qs.filter(standard_size=value)
            else:
                return qs

    price = django_filters.RangeFilter()
    size = SizeFilter(queryset=Size.objects.all(), widget=CheckboxSelectMultiple, label=_('Size'))

    def __init__(self, data=None, queryset=None, prefix=None, strict=None, category=None):
        super().__init__(data, queryset, prefix, strict)
        if category:
            self.sizes = category.size_set.size_set.all()
            self.filters['size'].field.queryset = self.sizes

    class Meta:
        model = Item
        fields = ['price']
        order_by = ['-updated_at', 'updated_at', 'price', '-price']

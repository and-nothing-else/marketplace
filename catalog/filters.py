import django_filters
from .models import Item


class ItemFilter(django_filters.FilterSet):
    price = django_filters.RangeFilter()

    class Meta:
        model = Item
        fields = ['price']
        order_by = ['-updated_at', 'updated_at', 'price', '-price']

from django.views.generic import DetailView
from django.shortcuts import get_object_or_404
from .models import Category, Item
from .filters import ItemFilter


class CatalogCategoryView(DetailView):
    model = Category
    context_object_name = 'category'
    template_name = 'catalog/category_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        items = self.get_object().item_set.active_for_location(self.request.location)
        # sort = self.request.GET.get('sort')
        # if sort in ['date', 'price']:
        #     if sort == 'date':
        #         sort = 'created_at'
        #     if self.request.GET.get('order') == 'desc':
        #         sort = '-' + sort
        #     f = f.order_by(sort)
        f = ItemFilter(self.request.GET, items)
        context['filter'] = f
        return context


class ItemDetailView(DetailView):
    model = Item
    context_object_name = 'item'
    template_name = 'catalog/item_detail.html'

    def get_object(self, queryset=None):
        return get_object_or_404(self.model, pk=self.kwargs['pk'], category__slug=self.kwargs['category_slug'])

from django.views.generic import DetailView
from django.shortcuts import get_object_or_404
from .models import Category, Item


class CatalogCategoryView(DetailView):
    model = Category
    context_object_name = 'category'
    template_name = 'catalog/category_detail.html'


class ItemDetailView(DetailView):
    model = Item
    context_object_name = 'item'
    template_name = 'catalog/item_detail.html'

    def get_object(self, queryset=None):
        return get_object_or_404(self.model, pk=self.kwargs['pk'], category__slug=self.kwargs['category_slug'])

from django.views.generic import DetailView
from .models import Category


class CatalogCategoryView(DetailView):
    model = Category
    context_object_name = 'category'
    template_name = 'catalog/category_detail.html'

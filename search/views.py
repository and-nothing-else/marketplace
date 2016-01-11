from django.views.generic import ListView
from django.db.models import Q
from catalog.models import Item


class CatalogSearchView(ListView):
    model = Item
    context_object_name = 'items'
    template_name = 'search/item_list.html'

    def get_queryset(self):
        q = self.request.GET.get('q', '')
        return self.model.objects.active().filter(
            Q(name__icontains=q) |
            Q(article=q)
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')
        return context

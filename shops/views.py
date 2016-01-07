from django.views.generic import ListView, DetailView
from .models import Shop


class ShopListView(ListView):
    model = Shop
    template_name = 'shops/shop_list.html'
    context_object_name = 'shops'

    def get_queryset(self):
        return self.request.location.shop_set.all()


class ShopDetailView(DetailView):
    model = Shop
    template_name = 'shops/shop_detail.html'
    context_object_name = 'shop'

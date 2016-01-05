from django.views.generic import UpdateView
from django.core.urlresolvers import reverse_lazy
from .models import Shop
from .forms import ShopForm


class ShopUpdateView(UpdateView):
    form_class = ShopForm
    template_name = 'profile/shop_update.html'
    success_url = reverse_lazy('profile:shop_update')

    def get_object(self, queryset=None):
        shop, created = Shop.objects.get_or_create(owner=self.request.user)
        return shop

from django.views.generic import UpdateView, ListView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from shops.models import Shop
from shops.forms import ShopForm
from tariff.models import Tariff
from marketplace.utils import int2semantic_ui_class


class ShopUpdateView(LoginRequiredMixin, UpdateView):
    form_class = ShopForm
    template_name = 'user/shop_update.html'
    success_url = reverse_lazy('user:shop_update')

    def get_object(self, queryset=None):
        shop, created = Shop.objects.get_or_create(owner=self.request.user)
        return shop


class TariffList(LoginRequiredMixin, ListView):
    model = Tariff
    template_name = 'user/tariff_select.html'
    context_object_name = 'tariffs'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tariff_count'] = int2semantic_ui_class(self.object_list.count())
        return context

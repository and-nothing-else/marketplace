from django.views.generic import UpdateView, ListView
from django.core.urlresolvers import reverse_lazy
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from extra_views import InlineFormSet, CreateWithInlinesView, UpdateWithInlinesView
from shops.models import Shop
from shops.forms import ShopForm
from tariff.models import Tariff
from catalog.models import Item, ItemPhoto
from catalog.forms import UserItemForm


class ShopUpdateView(LoginRequiredMixin, UpdateView):
    form_class = ShopForm
    template_name = 'user/shop_update.html'
    success_url = reverse_lazy('user:shop_update')

    def get_object(self, queryset=None):
        shop, created = Shop.objects.get_or_create(owner=self.request.user)
        return shop

    def get_initial(self):
        initial = super().get_initial()
        shop = self.get_object()
        initial['region'] = shop.region or self.request.location
        initial['slug'] = shop.slug or self.request.user.username
        return initial

    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS, _('Your shop info has been updated successfully'))
        return super().form_valid(form)


class TariffList(LoginRequiredMixin, ListView):
    model = Tariff
    template_name = 'user/tariff_select.html'
    context_object_name = 'tariffs'


class UserItemListView(LoginRequiredMixin, ListView):
    model = Item
    template_name = 'user/item_list.html'
    context_object_name = 'items'


class ItemPhotoInline(InlineFormSet):
    model = ItemPhoto
    fields = ['photo']


class UserItemCreateView(LoginRequiredMixin, CreateWithInlinesView):
    form_class = UserItemForm
    template_name = 'user/item_create.html'
    model = Item
    inlines = [ItemPhotoInline]

    def forms_valid(self, form, inlines):
        instance = form.save(commit=False)
        instance.shop = self.request.user.shop
        instance.save()
        messages.add_message(self.request, messages.SUCCESS,
                             _('%s has been added successfully' % instance.name)
                             )
        return super().forms_valid(form, inlines)


class UserItemUpdateView(LoginRequiredMixin, UpdateWithInlinesView):
    form_class = UserItemForm
    template_name = 'user/item_update.html'
    context_object_name = 'item'
    model = Item
    inlines = [ItemPhotoInline]

    def forms_valid(self, form, inlines):
        instance = form.save(commit=False)
        instance.shop = self.request.user.shop
        instance.save()
        messages.add_message(self.request, messages.SUCCESS,
                             _('%s has been updated successfully' % instance.name)
                             )
        return super().forms_valid(form, inlines)

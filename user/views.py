from django.views.generic import UpdateView, ListView
from django.core.urlresolvers import reverse_lazy
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import redirect
from extra_views import InlineFormSet, CreateWithInlinesView, UpdateWithInlinesView
from shops.models import Shop
from shops.forms import ShopForm
from tariff.models import Tariff
from catalog.models import Item, ItemPhoto, ItemCustomProperty
from catalog.forms import UserItemForm, UserItemPhotoForm


class ShopUpdateView(LoginRequiredMixin, UpdateView):
    form_class = ShopForm
    template_name = 'user/shop_update.html'
    success_url = reverse_lazy('user:shop_update')

    def get_object(self, queryset=None):
        try:
            shop = Shop.objects.get(owner=self.request.user)
        except Shop.DoesNotExist:
            shop = Shop(
                owner=self.request.user,
                slug=self.request.user.username
            )
            shop.save()
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


class MustHaveShopMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.shop:
            return redirect('user:shop_update')
        return super().dispatch(request, *args, **kwargs)


class TariffList(MustHaveShopMixin, ListView):
    model = Tariff
    template_name = 'user/tariff_select.html'
    context_object_name = 'tariffs'


class UserItemListView(MustHaveShopMixin, ListView):
    model = Item
    template_name = 'user/item_list.html'
    context_object_name = 'items'

    def get_queryset(self):
        return super().get_queryset().filter(shop__owner=self.request.user)


class ItemPhotoInline(InlineFormSet):
    model = ItemPhoto
    form_class = UserItemPhotoForm
    fields = ['photo', 'ordering']


class ItemPropertiesInline(InlineFormSet):
    model = ItemCustomProperty
    fields = ['name', 'value', 'ordering']


class UserItemViewMixin(MustHaveShopMixin):
    model = Item
    form_class = UserItemForm
    inlines = [ItemPhotoInline, ItemPropertiesInline]
    success_url = reverse_lazy('user:item_list')

    def forms_valid(self, form, inlines):
        instance = form.save(commit=False)
        instance.shop = self.request.user.shop
        user_items = self.request.user.shop.item_set.active()
        if instance.pk:
            user_items = user_items.exclude(pk=instance.pk)
        if user_items.count() >= instance.shop.owner.tariff.goods:
            instance.active = False
            messages.add_message(self.request, messages.ERROR, _("""
            <p>You have reached the maximum number of goods.</p>
            <p>Please <a href="%s">upgrade you tariff</a> to place more goods.
            """ % reverse_lazy('user:tariff_list')))
        instance.save()
        return super().forms_valid(form, inlines)


class UserItemCreateView(UserItemViewMixin, CreateWithInlinesView):
    template_name = 'user/item_create.html'

    def get_initial(self):
        initial = super().get_initial()
        initial['active'] = self.request.user.can_increase_active_items()
        return initial

    def forms_valid(self, form, inlines):
        messages.add_message(self.request, messages.SUCCESS,
                             _('%s has been added successfully' % form.instance.name)
                             )
        return super().forms_valid(form, inlines)


class UserItemUpdateView(UserItemViewMixin, UpdateWithInlinesView):
    template_name = 'user/item_update.html'

    def get_initial(self):
        initial = super().get_initial()
        if not self.request.user.can_increase_active_items() and not self.object.active:
            initial['active'] = False
        return initial

    def forms_valid(self, form, inlines):
        messages.add_message(self.request, messages.SUCCESS,
                             _('%s has been updated successfully' % form.instance.name)
                             )
        return super().forms_valid(form, inlines)

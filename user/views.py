from django.views.generic import UpdateView, ListView, TemplateView
from django.core.urlresolvers import reverse_lazy
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import redirect
from extra_views import InlineFormSet, NamedFormsetsMixin, CreateWithInlinesView, UpdateWithInlinesView
from shops.models import Shop
from shops.forms import ShopForm
from tariff.models import Tariff
from catalog.models import Category, Item, ItemPhoto, ItemCustomProperty, ItemSKU, ItemSKUSize, ItemSKUPhoto
from catalog.forms import UserItemForm, UserItemPhotoForm, UserItemCustomPropertyForm, \
    UserItemSKUForm, UserItemSKUSizeForm, UserItemSKUPhotoForm


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
    extra = 5


class ItemPropertiesInline(InlineFormSet):
    model = ItemCustomProperty
    form_class = UserItemCustomPropertyForm
    fields = ['name', 'value', 'ordering']


class UserItemViewMixin(MustHaveShopMixin, NamedFormsetsMixin):
    model = Item
    form_class = UserItemForm
    inlines = [ItemPropertiesInline]
    inlines_names = ['item_property_inline']
    success_url = reverse_lazy('user:item_list')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        if self.category.sku_allowed:
            del form.fields['color']
            del form.fields['standard_size']
            del form.fields['size']
        else:
            self.inlines.append(ItemPhotoInline)
            self.inlines_names.append('item_photo_inline')
            sizes = self.category.get_sizes()
            if sizes:
                form.fields['standard_size'].queryset = sizes
            else:
                del form.fields['standard_size']
                del form.fields['size']
        return form

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


class UserItemSelectCategoryView(MustHaveShopMixin, TemplateView):
    template_name = 'user/item_create_category_select.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.get_annotated_list(max_depth=2)
        return context


class UserItemCreateView(UserItemViewMixin, CreateWithInlinesView):
    template_name = 'user/item_create.html'
    category = None

    def dispatch(self, request, *args, **kwargs):
        self.category = Category.objects.get(pk=kwargs.get('category_id'))
        return super().dispatch(request, *args, **kwargs)

    def get_initial(self):
        initial = super().get_initial()
        initial['active'] = self.request.user.can_increase_active_items()
        return initial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        return context

    def forms_valid(self, form, inlines):
        instance = form.save(commit=False)
        instance.category = self.category
        instance.shop = self.request.user.shop
        instance.save()
        if self.request.POST.get('next') == 'sku':
            self.success_url = reverse_lazy('user:item_create_sku', args=[instance.pk])
        messages.add_message(self.request, messages.SUCCESS,
                             _('%s has been added successfully' % form.instance.name)
                             )
        return super().forms_valid(form, inlines)


class UserItemUpdateView(UserItemViewMixin, UpdateWithInlinesView):
    template_name = 'user/item_update.html'

    def dispatch(self, request, *args, **kwargs):
        self.category = self.get_object().category
        return super().dispatch(request, *args, **kwargs)

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


class ItemSKUSizeInline(InlineFormSet):
    model = ItemSKUSize
    form_class = UserItemSKUSizeForm
    fields = ['size', 'standard_size']
    extra = 5


class ItemSKUPhotoInline(InlineFormSet):
    model = ItemSKUPhoto
    form_class = UserItemSKUPhotoForm
    extra = 5


class SKUMixin(MustHaveShopMixin, NamedFormsetsMixin):
    item = None
    model = ItemSKU
    form_class = UserItemSKUForm
    inlines = [ItemSKUSizeInline, ItemSKUPhotoInline]
    inlines_names = ['sku_size_inline', 'sku_photo_inline']
    success_url = reverse_lazy('user:item_list')

    def dispatch(self, request, *args, **kwargs):
        self.item = Item.objects.get(pk=kwargs.get('item_id'))
        return super().dispatch(request, *args, **kwargs)

    def construct_inlines(self):
        sizes = self.item.category.get_sizes()
        inline_formsets = []
        for inline_class in self.get_inlines():
            inline_instance = inline_class(self.model, self.request, self.object, self.kwargs, self)
            inline_formset = inline_instance.construct_formset()
            for f in inline_formset:
                try:
                    f.fields['standard_size'].queryset = sizes
                except KeyError:
                    pass
            inline_formsets.append(inline_formset)
        return inline_formsets

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['item'] = self.item
        return context

    def forms_valid(self, form, inlines):
        instance = form.save(commit=False)
        instance.item = self.item
        instance.save()
        if self.request.POST.get('next') == 'sku':
            self.success_url = reverse_lazy('user:item_create_sku', args=[self.item.id])
        messages.add_message(self.request, messages.SUCCESS,
                             _('SKU for %s has been added successfully' % self.item.name)
                             )
        return super().forms_valid(form, inlines)


class UserItemSKUCreateView(SKUMixin, CreateWithInlinesView):
    template_name = 'user/item_sku_create.html'


class UserItemSKUUpdateView(SKUMixin, UpdateWithInlinesView):
    template_name = 'user/item_sku_update.html'

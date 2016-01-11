from django import template
from ..models import Category, Item

register = template.Library()


@register.inclusion_tag('catalog/catalog_menu.html', takes_context=True)
def catalog_menu(context):
    category_list = Category.get_annotated_list(max_depth=2)
    return {
        'category_list': category_list
    }


@register.inclusion_tag('catalog/_catalog_item_card_list.html', takes_context=True)
def catalog_latest_goods(context, number=4):
    items = Item.objects.active_for_location(context['request'].location)[:number]
    return {
        'items': items
    }


@register.inclusion_tag('catalog/shop_goods.html', takes_context=True)
def catalog_shop_goods(context, shop_id, number=4):
    items = Item.objects.active().filter(shop__id=shop_id)[:number]
    return {
        'items': items
    }


@register.inclusion_tag('catalog/sort.html', takes_context=True)
def catalog_sort(context):
    params_for_date = context['request'].GET.copy()
    params_for_price = context['request'].GET.copy()
    current_ordering = context['request'].GET.get('o', '-created_at')
    params_for_date['o'] = 'created_at' if context['request'].GET.get('o') == '-created_at' else '-created_at'
    params_for_price['o'] = '-price' if context['request'].GET.get('o') == 'price' else 'price'
    return {
        'current_ordering': current_ordering,
        'date_link': params_for_date.urlencode(),
        'price_link': params_for_price.urlencode(),
    }

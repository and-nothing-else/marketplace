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
    items = Item.objects.active()[:number]
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
    params = context['request'].GET
    return {
        'sort': params.get('sort'),
        'order': params.get('order')
    }

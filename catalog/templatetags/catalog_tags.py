from django import template
from ..models import Category

register = template.Library()


@register.inclusion_tag('catalog/catalog_menu.html', takes_context=True)
def catalog_menu(context):
    category_list = Category.get_annotated_list(max_depth=2)
    return {
        'category_list': category_list
    }

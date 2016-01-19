from django import template
from django.contrib.messages import get_messages

register = template.Library()


@register.inclusion_tag('user/profile_menu.html', takes_context=True)
def profile_menu(context):
    return {
        'user': context['request'].user
    }


@register.inclusion_tag('user/balance_card.html', takes_context=True)
def my_balance_card(context):
    return {
        'user': context['request'].user
    }


@register.inclusion_tag('user/messages.html', takes_context=True)
def messages(context):
    return {
        'user': context['request'].user,
        'messages': get_messages(context['request'])
    }


@register.inclusion_tag('user/item_create_steps.html', takes_context=True)
def item_create_steps(context, active_step=1, sku_allowed=True):
    return {
        'active_step': active_step,
        'sku_allowed': sku_allowed,
        'steps': [
            ['Выбор раздела', 'только при создании товара'],
            ['Информация о товаре', 'основное'],
            ['Торговые предложения', 'цвет и размеры'],
        ]
    }

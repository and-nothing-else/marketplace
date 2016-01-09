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


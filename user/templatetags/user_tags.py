from django import template

register = template.Library()


@register.inclusion_tag('user/profile_menu.html', takes_context=True)
def profile_menu(context):
    return {
    }


@register.inclusion_tag('user/balance_card.html', takes_context=True)
def my_balance_card(context):
    return {
        'user': context['request'].user
    }

from django import template

register = template.Library()


@register.inclusion_tag('tariff/my_tariff_card.html', takes_context=True)
def my_tariff_card(context):
    return {
        'tariff': context['request'].user.get_tariff()
    }

from django import template
from ..models import Region

register = template.Library()


@register.inclusion_tag('dictionary/region_switcher.html', takes_context=True)
def region_switcher(context):
    return {
        'location': context['request'].location,
        'regions': Region.get_available_locations()
    }

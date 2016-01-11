from django import template
from ..models import SuperBanner

register = template.Library()


@register.inclusion_tag('superbanner/superbanner.html')
def superbanner():
    return {
        'banners': SuperBanner.objects.all()
    }


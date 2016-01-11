from django import template

register = template.Library()


@register.inclusion_tag('search/search_form.html', takes_context=True)
def search_form(context):
    return {
        'q': context['request'].GET.get('q', '')
    }


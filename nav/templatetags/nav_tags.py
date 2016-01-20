from django import template

register = template.Library()


@register.inclusion_tag('nav/breadcrumb.html', takes_context=True)
def breadcrumb(context, path=None):
    return {
        'path': path
    }

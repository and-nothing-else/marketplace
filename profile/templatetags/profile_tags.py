from django import template

register = template.Library()


@register.inclusion_tag('profile/profile_menu.html', takes_context=True)
def profile_menu(context):
    return {
    }

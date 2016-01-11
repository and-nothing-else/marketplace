from django import template
from ..models import Article

register = template.Library()


@register.inclusion_tag('articles/main_articles.html', takes_context=True)
def main_articles(context, number=2):
    return {
        'articles': Article.objects.active()[:number]
    }

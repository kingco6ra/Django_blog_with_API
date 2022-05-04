from django import template
from django.db.models import Count
from news_app.models import Category
from django.core.cache import cache

# регистрация template тэга
register = template.Library()


@register.inclusion_tag('list_categories.html')
def show_categories():
    categories = cache.get('categories')
    if not categories:
        categories = Category.objects.all().annotate(cnt=Count('news')).filter(cnt__gt=0)
        cache.set('categories', categories, 30)
    return {'categories': categories}

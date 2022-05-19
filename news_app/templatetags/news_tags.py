from django import template
from django.db.models import Count
from news_app.models import Category

# регистрация template тэга
register = template.Library()


@register.inclusion_tag('list_categories.html')
def show_categories():
    categories = Category.objects.all().annotate(cnt=Count('news_category')).filter(cnt__gt=0)
    return {'categories': categories}

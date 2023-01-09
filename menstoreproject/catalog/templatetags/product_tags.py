from django import template
from catalog.models import Category, Product


register = template.Library()


@register.inclusion_tag('catalog/list_categories.html')
def show_categories():
    categories = Category.objects.all()
    return {'categories': categories}

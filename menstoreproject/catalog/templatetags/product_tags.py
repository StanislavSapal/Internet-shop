from django import template
from catalog.models import Category, Product
from django.db.models import *
from django.core.cache import cache

register = template.Library()


@register.simple_tag(name='get_list_categories')
def get_categories():
    return Category.objects.all()


@register.inclusion_tag('catalog/list_categories.html')
def show_categories():
    categories = Category.objects.all()
    return {'categories': categories}

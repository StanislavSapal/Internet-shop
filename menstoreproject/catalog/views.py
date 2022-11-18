from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import render, get_object_or_404, redirect

from catalog.models import *


def index(request):
    return render(request, 'catalog/index.html')


# class ViewProduct(DetailView):
#     model = Product
#     product_item = Product.objects.get(pk=product_id)
#     template_name = 'catalog/product_detail.html'


def view_product(request, product_id):
    product_item = get_object_or_404(Product, pk=product_id)
    return render(request, 'news/view_news.html', {'product_item': product_item})



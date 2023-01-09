from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import render, get_object_or_404, redirect
from .models import *


def index(request):
    return render(request, 'catalog/index.html')


class ViewProduct(DetailView):
    model = Product
    context_object_name = 'product_item'


class ProductsView(ListView):
    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        if self.kwargs.get('category_slug'):
            return Product.objects.filter(category__slug=self.kwargs['category_slug'])
        else:
            return Product.objects.all()

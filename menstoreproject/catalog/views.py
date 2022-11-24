from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import render, get_object_or_404, redirect
from .models import *


def index(request):
    return render(request, 'catalog/index.html')


class ViewProduct(DetailView):
    model = Product
    context_object_name = 'product_item'


class ProductList(ListView):
    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'products'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self):
        return Product.objects.select_related('category')


class ProductByCategory(ListView):
    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'products'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self):
        return Product.objects.filter(category_id=self.kwargs['category_id']).select_related('category')


from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import render, get_object_or_404, redirect

from catalog.models import *


def index(request):
    return render(request, 'catalog/index.html')


class ViewProduct(DetailView):
    model = Product
    context_object_name = 'product_item'




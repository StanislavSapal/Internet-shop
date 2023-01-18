from django.shortcuts import render
from .models import *


def cart_view(request):
    cart = Cart.objects.all().first()
    return render(request, 'cart/cart_detail.html', {'cart': cart})

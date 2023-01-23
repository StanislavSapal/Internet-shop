from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from django.db.models import F, Sum
from .models import *


class CartPageView(DetailView):
    model = Cart

    def get_object(self):
        return get_object_or_404(Cart, user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart_items'] = self.object.cartitem_set.all()
        context['cart'] = Cart.objects.annotate(price=Sum(F('cartitem__product__price') * F('cartitem__quantity'))
        ).get(user=self.request.user)
        return context


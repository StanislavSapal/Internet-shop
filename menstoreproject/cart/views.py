from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from rest_framework import viewsets, mixins
from rest_framework.exceptions import ValidationError
from rest_framework import permissions
from .permissions import IsOwner
from .serializers import *


class CartPageView(DetailView):
    model = Cart

    def get_object(self, queryset=None):
        return self.request.cart

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart_items'] = self.object.cartitem_set.all()
        context['total_cart_sum'] = self.object.cartitem_set.aggregate(price_total=Sum(F('product__price') *
                                                                                       F('quantity')))
        return context


class CartItemViewSet(mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      viewsets.GenericViewSet):

    queryset = CartItem.objects.all()
    serializer_class = CartListSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get_cart(self):
        cart = self.request.cart
        if not cart:
            raise ValidationError("You don't have cart. Create it first")
        return cart

    def perform_create(self, serializer):
        serializer.save(cart=self.get_cart())


class CartViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

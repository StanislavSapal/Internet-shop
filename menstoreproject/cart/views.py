from django.shortcuts import get_object_or_404
from django.views.generic import DetailView

from rest_framework import viewsets, mixins, generics
from rest_framework.exceptions import ValidationError

from rest_framework import permissions

from .permissions import IsOwner
from .serializers import *


class CartPageView(DetailView):
    model = Cart

    def get_object(self):
        return get_object_or_404(Cart, user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart_items'] = self.object.cartitem_set.all()
        context['total_cart_sum'] = self.object.cartitem_set.aggregate(price_total=Sum(F('product__price') *
                                                                                       F('quantity')))
        return context


class CartItemViewSet(viewsets.GenericViewSet,
                      mixins.ListModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin):

    queryset = CartItem.objects.all()
    serializer_class = CartListSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get_cart(self):
        cart = Cart.objects.filter(user=self.request.user, status='O').last()
        if not cart:
            raise ValidationError('You have no cart. Create it first')
        return cart

    def perform_create(self, serializer):
        serializer.save(cart=self.get_cart())


class CartViewSet(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    @classmethod
    def get_extra_actions(cls):
        return []

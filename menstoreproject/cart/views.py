from django.views.generic import DetailView
from rest_framework import viewsets, mixins
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


class CartItemViewSet(mixins.CreateModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      viewsets.GenericViewSet):

    queryset = CartItem.objects.all()
    serializer_class = CartListSerializer
    permission_classes = [IsOwner]

    def perform_create(self, serializer):
        serializer.save(cart=self.request.cart)


class CartViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

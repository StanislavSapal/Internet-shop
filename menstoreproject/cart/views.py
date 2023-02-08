from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from django.db.models import F, Sum
from rest_framework import viewsets

from .models import *

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


class CartItemViewSet(viewsets.ModelViewSet):

    queryset = CartItem.objects.all()
    serializer_class = CartListSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def perform_create(self, serializer):
        # when a product is saved, its saved how it is the owner
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        # after get all products on DB it will be filtered by its owner and return the queryset
        owner_queryset = self.queryset.filter(owner=self.request.user)
        return owner_queryset

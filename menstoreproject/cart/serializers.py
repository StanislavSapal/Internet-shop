from rest_framework import serializers
from .models import *


class CartListSerializer(serializers.ModelSerializer):
    cart = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = CartItem
        fields = ('id', 'cart', 'product', 'quantity')


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ('user', 'status', 'total_cart_sum')

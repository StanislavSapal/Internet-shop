from rest_framework import serializers

from .models import CartItem


class CartListSerializer(serializers.ModelSerializer):

    class Meta:
        model = CartItem
        fields = ('id', 'cart', 'product', 'quantity')

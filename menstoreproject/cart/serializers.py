from rest_framework import serializers

from .models import CartItem


class CartListSerializer(serializers.ModelSerializer):
    cart = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = CartItem
        fields = ('id', 'cart', 'product', 'quantity')


from rest_framework import serializers
from .models import *


class CartListSerializer(serializers.ModelSerializer):
    cart = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = CartItem
        fields = ('id', 'cart', 'product', 'quantity', 'size')

    def validate(self, attrs):
        if 'product' in attrs:
            product = attrs['product']
            if product.size.all() and not attrs['size']:
                raise serializers.ValidationError()
        return attrs


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ('user', 'status', 'total_cart_sum')

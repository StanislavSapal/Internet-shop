from collections import OrderedDict

from django.test import TestCase
from cart.serializers import CartSerializer, CartListSerializer
from cart.models import Cart, CartItem
from catalog.models import *


class CartSerializerTestCase(TestCase):
    def test_data(self):
        cart_1 = Cart.objects.create()
        cart_2 = Cart.objects.create()
        data = CartSerializer([cart_1, cart_2], many=True).data
        expected_data = [
            OrderedDict([
                ('user', None),
                ('status', 'Open'),
                ('total_cart_sum', {'price_total': None})
            ]),
            OrderedDict([
                ('user', None),
                ('status', 'Open'),
                ('total_cart_sum', {'price_total': None})
            ])
        ]
        self.assertEqual(expected_data, data)


class CartListSerializerTestCase(TestCase):
    def test_data(self):
        category_1 = Category.objects.create(title='category name',
                                             slug='category name',
                                             image='',
                                             description='category decription text')
        product_1 = Product.objects.create(name='product_1', slug='product_1', category=category_1,
                                           description='product_1 decription text', price=500, material='cotton',
                                           quantity=5, top_seller=True, selected=False)
        product_2 = Product.objects.create(name='product_2', slug='product_2', category=category_1,
                                           description='product_2 decription text', price=500, material='animal skin',
                                           quantity=7, top_seller=False, selected=False)
        cart_1 = Cart.objects.create()
        cart_item_1 = CartItem.objects.create(cart=cart_1, product=product_1, quantity=1, size='')
        cart_item_2 = CartItem.objects.create(cart=cart_1, product=product_2, quantity=1, size='')
        data = CartListSerializer([cart_item_1, cart_item_2], many=True).data
        expected_data = [
            OrderedDict([
                ('id', 1),
                ('cart', 1),
                ('product', 1),
                ('quantity', 1),
                ('size', '')
            ]),
            OrderedDict([
                ('id', 2),
                ('cart', 1),
                ('product', 2),
                ('quantity', 1),
                ('size', '')
            ])
        ]
        self.assertEqual(expected_data, data)

from django.test import TestCase
from cart.models import *
from cart.middlewares import generate_token
from catalog.models import Category, Product


class CartModelTestCase(TestCase):

    def test_cart_status(self):
        cart = Cart.objects.create()
        self.assertEqual(cart.status, 'Open')

    def test_token(self):
        cart = Cart.objects.create(token=generate_token())
        self.assertEqual(len(cart.token), 16)


class CartItemModelTestCase(TestCase):

    def test_cartitem_sum(self):
        category_1 = Category.objects.create(title='category name',
                                             slug='category name',
                                             image='',
                                             description='category decription text')
        product_1 = Product.objects.create(name='product_1', slug='product_1', category=category_1,
                                           description='product_1 decription text', price=500, material='cotton',
                                           quantity=5, top_seller=True, selected=False)
        cart_1 = Cart.objects.create()
        cart_item_1 = CartItem.objects.create(cart=cart_1, product=product_1, quantity=3, size='')
        self.assertEqual(cart_item_1.total_item_price, 1500)

from django.test import TestCase
from django.test.client import RequestFactory
from django.contrib.auth.models import User
from unittest.mock import patch, MagicMock, Mock
from cart.middlewares import *


class CartMiddlewareTest(TestCase):
    def setUp(self):
        self.middleware = CartMiddleware(lambda req: HttpResponse())

    @patch('cart.middlewares.get_cart_by_user')
    def test_authenticated_user_with_existing_cart(self, mock_get_cart_by_user):
        user = User.objects.create(username='testuser')
        cart = MagicMock()
        mock_get_cart_by_user.return_value = cart
        request = RequestFactory().get('/')
        request.user = user
        response = self.middleware(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(request.cart, cart)
        mock_get_cart_by_user.assert_called_once_with(user)

    @patch('cart.middlewares.get_cart_by_user')
    def test_authenticated_user_without_cart(self, mock_get_cart_by_user):
        user = User.objects.create(username='testuser')
        mock_get_cart_by_user.return_value = None
        request = RequestFactory().get('/')
        request.user = user
        response = self.middleware(request)
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(request.cart.id)
        mock_get_cart_by_user.assert_called_once_with(user)

    @patch('cart.middlewares.get_cart_by_token')
    def test_anonymous_user_with_token(self, mock_get_cart_by_token):
        user = Mock()
        user.is_authenticated = False
        token = 'testtoken'
        cart = MagicMock()
        mock_get_cart_by_token.return_value = cart
        request = RequestFactory().get('/')
        request.user = user
        request.session = {'token': token}
        response = self.middleware(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(request.cart, cart)
        mock_get_cart_by_token.assert_called_once_with(token)

    @patch('cart.middlewares.create_cart_for_anonymous_user')
    def test_anonymous_user_without_token(self, mock_create_cart_for_anonymous_user):
        user = Mock()
        user.is_authenticated = False
        token = 'testtoken'
        cart = MagicMock()
        mock_create_cart_for_anonymous_user.return_value = cart
        request = RequestFactory().get('/')
        request.user = user
        request.session = {'token': token}
        response = self.middleware(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(request.cart, cart)
        mock_create_cart_for_anonymous_user.assert_called_once_with(request)

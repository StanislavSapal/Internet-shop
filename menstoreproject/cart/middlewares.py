from .models import Cart
from django.utils.functional import SimpleLazyObject
import random
import string


def get_cart_by_user(user):
    cart = Cart.objects.filter(user=user, status=Cart.StatusChoices.OPEN).last()
    return cart


def generate_token():
    token = ''.join(random.choice(string.ascii_letters) for i in range(16))
    return token


def get_cart_by_token(token):
    cart = Cart.objects.filter(token=token, status=Cart.StatusChoices.OPEN).last()
    return cart


def create_cart_for_anonymous_user(request):
    new_token = generate_token()
    request.session['token'] = new_token
    cart = Cart(token=new_token)
    cart.save()
    return cart


class CartMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            if hasattr(request, 'cart'):
                response = self.get_response(request)
                return response
            else:
                cart = SimpleLazyObject(lambda: get_cart_by_user(request.user))
                if not cart:
                    cart = Cart(user=request.user)
                    cart.save()
                request.cart = cart
        else:
            if request.session.get('token'):
                cart = SimpleLazyObject(lambda: get_cart_by_token(request.session['token']))
                if not cart:
                    cart = create_cart_for_anonymous_user(request)
            else:
                cart = create_cart_for_anonymous_user(request)
            request.cart = cart
        response = self.get_response(request)
        return response

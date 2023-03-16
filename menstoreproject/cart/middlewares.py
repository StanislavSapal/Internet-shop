from .models import Cart
from django.utils.functional import SimpleLazyObject


def get_cart(user):
    cart = Cart.objects.filter(user=user, status=Cart.StatusChoices.OPEN).last()
    print('finding of a cart')
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
                cart = SimpleLazyObject(lambda: get_cart(request.user))
                if cart:
                    request.cart = cart
                else:
                    cart = Cart(user=request.user)
                    cart.save()
                    request.cart = cart
        else:
            pass
        response = self.get_response(request)
        return response

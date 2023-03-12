from .models import Cart


class CartMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            cart = Cart.objects.filter(user=request.user, status=Cart.StatusChoices.OPEN).last()
            if cart:
                request.cart = cart
            else:
                cart = Cart(user=request.user)
                cart.save()
                request.cart = cart
        else:
            request.cart = None
        response = self.get_response(request)
        return response

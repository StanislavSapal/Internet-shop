

def add_variable_to_context(request):
    return {
        'cart_items': request.cart.cartitem_set.all()
    }

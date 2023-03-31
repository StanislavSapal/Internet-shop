

def cart_items_count(request):
    return {
        'cart_items': request.cart.cartitem_set.all()
    }

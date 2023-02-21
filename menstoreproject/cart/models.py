from django.db import models
from django.db.models import F, Sum
from menstoreproject.models import TimeStampedModel


class Cart(TimeStampedModel):
    CART_STATUS_CHOICES = (
        ('O', 'Open'),
        ('C', 'Closed')
    )
    user = models.ForeignKey('authentication.User', on_delete=models.CASCADE)
    status = models.CharField(choices=CART_STATUS_CHOICES,  max_length=50)

    @property
    def total_cart_sum(self):
        return self.cartitem_set.aggregate(price_total=Sum(F('product__price') * F('quantity')))


class CartItem(TimeStampedModel):
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE)
    product = models.ForeignKey('catalog.Product', on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.IntegerField()

    @property
    def total_item_price(self):
        return self.quantity * self.product.price

    @property
    def owner(self):
        return self.cart.user 

from django.db import models

from menstoreproject.models import TimeStampedModel


class Cart(TimeStampedModel):
    CART_STATUS_CHOICES = (
        ('O', 'Open'),
        ('C', 'Closed')
    )
    user = models.ForeignKey('authentication.User', on_delete=models.CASCADE)
    status = models.CharField(choices=CART_STATUS_CHOICES,  max_length=50)


class CartItem(TimeStampedModel):
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE)
    product = models.ForeignKey('catalog.Product', on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField()

    def get_total_item_price(self):
        return self.quantity * self.product.price

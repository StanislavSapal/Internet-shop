from django.db import models
from django.db.models import F, Sum
from menstoreproject.models import TimeStampedModel


class Cart(TimeStampedModel):
    class StatusChoices(models.TextChoices):
        OPEN = 'Open'
        CLOSED = 'Closed'

    user = models.ForeignKey('authentication.User', on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=StatusChoices.choices, default=StatusChoices.OPEN)

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

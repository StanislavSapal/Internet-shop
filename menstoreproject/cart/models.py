from django.db import models
from django.db.models import F, Sum
from menstoreproject.models import TimeStampedModel


class Cart(TimeStampedModel):
    class StatusChoices(models.TextChoices):
        open = 'Open'
        closed = 'Closed'

    user = models.ForeignKey('authentication.User', on_delete=models.CASCADE, blank=True, null=True)
    status = models.CharField(max_length=10, choices=StatusChoices.choices, default=StatusChoices.open)
    token = models.CharField(blank=True, null=True, max_length=16, unique=True)

    @property
    def total_cart_sum(self):
        return self.cartitem_set.aggregate(price_total=Sum(F('product__price') * F('quantity')))


class CartItem(TimeStampedModel):
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE)
    product = models.ForeignKey('catalog.Product', on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.IntegerField()
    size = models.CharField(max_length=5, blank=True, null=True, verbose_name='Розмір')

    @property
    def total_item_price(self):
        return self.quantity * self.product.price

    @property
    def owner(self):
        return self.cart.user or self.cart.token

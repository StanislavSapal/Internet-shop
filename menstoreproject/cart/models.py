from django.db import models


class Cart(models.Model):
    CART_STATUS_CHOICES = (
        ('O', 'Open'),
        ('C', 'Closed')
    )
    user = models.ForeignKey('User', on_delete=models.PROTECT)
    status = models.CharField(choices=CART_STATUS_CHOICES)


class CartItem(models.Model):
    user = models.ForeignKey('User', on_delete=models.PROTECT)
    cart = models.ForeignKey('Cart', on_delete=models.PROTECT)
    quantity = models.IntegerField(default=0)

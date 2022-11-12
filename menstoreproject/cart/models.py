from django.db import models


class Cart(models.Model):
    CART_STATUS_CHOICES = (
        ('O', 'Open'),
        ('C', 'Closed')
    )
    user = models.ForeignKey('authentication.User', on_delete=models.CASCADE)
    status = models.CharField(choices=CART_STATUS_CHOICES, max_length=50)


class CartItem(models.Model):
    user = models.ForeignKey('authentication.User', on_delete=models.CASCADE)
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE)
    quantity = models.IntegerField()

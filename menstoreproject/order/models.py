from django.db import models


class Order:
    cart = models.ForeignKey('cart.Cart', on_delete=models.PROTECT)
    first_name = models.CharField(max_length=50, blank=False, null=False)
    last_name = models.CharField(max_length=50, blank=False, null=False)
    phone = models.CharField(blank=False, null=False)
    address = models.CharField(blank=False, null=False)
    email = models.EmailField(blank=False, null=False)


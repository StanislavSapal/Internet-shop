from django.db import models

from menstoreproject.models import TimeStampedModel


class Order(TimeStampedModel):
    cart = models.ForeignKey('cart.Cart', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(blank=True)
    address = models.CharField(blank=True)
    email = models.EmailField(blank=True)


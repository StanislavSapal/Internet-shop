from django.db import models
from menstoreproject.models import TimeStampedModel
import random


def generate_order_number():
    nums = [random.randint(0, 9) for _ in range(9)]
    order_number = '{}{}{} {}{}{} {}{}{}'.format(*nums)
    return order_number


class Order(TimeStampedModel):
    class StatusChoices(models.TextChoices):
        DONE = 'Виконано'
        IN_PROGRESS = 'Виконується'
        CANCELLED = 'Скасовано'

    cart = models.ForeignKey('cart.Cart', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(blank=True, max_length=50)
    town = models.CharField(max_length=250)
    region = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    email = models.EmailField(blank=True)
    order_number = models.CharField(max_length=11, unique=True)
    status = models.CharField(max_length=11, choices=StatusChoices.choices, default=StatusChoices.IN_PROGRESS)
    comment = models.TextField(blank=True, null=True, max_length=500)

    def save(self, *args, **kwargs):
        if not self.order_number:
            self.order_number = generate_order_number()
        super(Order, self).save(*args, **kwargs)

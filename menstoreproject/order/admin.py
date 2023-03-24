from django.contrib import admin
from .models import *


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'cart', 'first_name', 'last_name', 'phone', 'email', 'town', 'region', 'address',
                    'order_number', 'status')

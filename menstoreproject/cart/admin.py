from django.contrib import admin
from .models import *


class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'status')


class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart', 'product', 'quantity')


admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem, CartItemAdmin)

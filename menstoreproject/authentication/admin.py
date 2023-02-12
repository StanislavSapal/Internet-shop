from django.contrib import admin
from .models import User


@admin.register(User)
class CartUser(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'first_name', 'last_name')

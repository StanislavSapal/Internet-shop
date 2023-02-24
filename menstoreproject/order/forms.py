from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['cart', 'first_name', 'last_name', 'phone', 'email',  'town', 'region', 'address']

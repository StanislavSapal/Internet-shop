from django.core.exceptions import ValidationError
from .models import Order
import re
from django import forms


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['cart', 'first_name', 'last_name', 'phone', 'email',  'town', 'region', 'address']
        widgets = {
            'cart': forms.NumberInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'town': forms.TextInput(attrs={'class': 'form-control'}),
            'region': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        if re.search(r'\d', first_name):
            raise ValidationError("Ім'я не може містити цифр")
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        if re.search(r'\d', last_name):
            raise ValidationError('Прізвище не може містити цифр')
        return last_name

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if not re.match(r'^\+380\d{9}$', phone):
            raise ValidationError('Номер телефону має починатися з "+380"!')
        return phone

    def clean_email(self):
        email = self.cleaned_data['email']
        if not re.match("\S+@\S+\.\S+", email):
            raise forms.ValidationError(
                code="invalid",
                message="Введіть email коректно"
            )
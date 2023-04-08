from django import forms
from django.core.mail import send_mail


class ContactForm(forms.Form):
    name = forms.CharField(label="Ваше ім'я", widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="Ваша email-адреса",
                             widget=forms.EmailInput(attrs={'autocomplete': 'off',
                                                            'class': 'form-control',
                                                            'placeholder': 'example@mail.com',
                                                            'required': 'required'}),
                             error_messages={'invalid': 'Введіть коректну email адресу'})
    subject = forms.CharField(label="Тема",
                              widget=forms.TextInput(attrs={'class': 'form-control'}))
    message = forms.CharField(label="Ваше повідомленя",
                              widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))

    def send_email(self):
        user_message = "{name} / {email} said: ".format(name=self.cleaned_data.get('name'),
                                                        email=self.cleaned_data.get('email'))
        user_message += "\n\n{0}".format(self.cleaned_data.get('message'))
        send_mail(self.cleaned_data['subject'], user_message, 'sapalstanislav@ukr.net',
                  ['sapals.rozetka@gmail.com'], fail_silently=False)

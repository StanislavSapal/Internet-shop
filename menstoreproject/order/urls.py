from django.urls import path, include
from .views import *

urlpatterns = [
    path('checkout/', OrderConfirmationView.as_view(), name='checkout_page'),
    path('checkout/done/', done, name='done'),
]

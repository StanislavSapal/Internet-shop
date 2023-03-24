from django.urls import path
from .views import *

urlpatterns = [
    path('checkout/', OrderConfirmationView.as_view(), name='checkout'),
    path('checkout/success/', successful_order_page_view, name='successful_order'),
    path('orders/', OrderList.as_view(), name='orders'),
]

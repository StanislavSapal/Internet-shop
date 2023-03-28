from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('checkout/', OrderConfirmationView.as_view(), name='checkout'),
    path('checkout/success/', successful_order_page_view, name='successful_order'),
    path('orders/', login_required(OrderList.as_view()), name='orders'),
]

from django.urls import path
from .views import *

urlpatterns = [
    path('checkout/', OrderConfirmationView.as_view(), name='checkout'),
    path('checkout/success/', successful_order_page_view, name='successful_order'),
    path('user_orders/', UserOrderList.as_view(), name='user_orders'),
    path('all_orders/', OrderList.as_view(), name='all_orders'),
]

from django.urls import path, include
from .views import *

from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'cartitems', CartItemViewSet)

urlpatterns = [
    path('cart/', CartPageView.as_view(), name='cart'),
    path("api/v1/", include(router.urls)),
]

from django.urls import path, include
from .views import *

from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'cartitems', CartItemViewSet)

urlpatterns = [
    path('cart/', CartPageView.as_view(), name='cart'),
    path("api/v1/", include(router.urls)),
    # path('cartitems/', CartItemViewSet.as_view({'get': 'list'})),
    # path('cartitems/<int:pk>/', CartItemViewSet.as_view({'put': 'update'})),
]
from django.urls import path
from .views import *


urlpatterns = [
    path('cart/', CartPageView.as_view(), name='cart'),
]
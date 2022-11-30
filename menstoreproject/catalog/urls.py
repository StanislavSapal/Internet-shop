from django.urls import path
from .views import *


urlpatterns = [
    path('product/<int:pk>/', ViewProduct.as_view(), name='view_product'),
]


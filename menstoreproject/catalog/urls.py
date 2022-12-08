from django.urls import path
from .views import *


urlpatterns = [
    path('product/<slug:slug>/', ViewProduct.as_view(), name='view_product'),
]


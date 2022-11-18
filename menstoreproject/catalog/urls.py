from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='home'),
    path('product/<int:product_id>/', view_product, name='view_product')
]

from django.urls import path
from .views import *


urlpatterns = [
    path('product/<slug:slug>/', ViewProduct.as_view(), name='view_product'),
    path('products/', ProductsView.as_view(), name='list_of_products'),
    path('products/<slug:category_slug>/', ProductsView.as_view(), name='products_by_category')
]


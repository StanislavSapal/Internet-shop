from django.urls import path
from .views import *


urlpatterns = [
    path('product/<slug:slug>/', ViewProduct.as_view(), name='view_product'),
    path('category/<slug:category_slug>/', ProductByCategory.as_view(extra_context={'title': 'Обрана категорія'}),
         name='category')
]


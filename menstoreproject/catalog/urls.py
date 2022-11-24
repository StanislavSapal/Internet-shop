from django.urls import path
from .views import *


urlpatterns = [
    path('', ProductList.as_view(), name='home'),
    path('product/<int:pk>/', ViewProduct.as_view(), name='view_product'),
    path('category/<int:category_id>/', ProductByCategory.as_view(extra_context={'title': 'Обрана категорія'}),
         name='category')
]


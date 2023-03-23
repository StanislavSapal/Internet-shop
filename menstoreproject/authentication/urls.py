from django.urls import path
from .views import signup_redirect, user_logout

urlpatterns = [
    path('social/signup/', signup_redirect, name='signup_redirect'),
    path('logout/', user_logout, name='logout')
]
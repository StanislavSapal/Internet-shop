from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib import messages


def signup_redirect(request):
    messages.error(request, "Something wrong here, it may be that you already have account!")
    return redirect('home')


def user_logout(request):
    logout(request)
    return redirect('home')

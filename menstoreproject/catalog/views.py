from django.shortcuts import render
from django.http import HttpResponse

from catalog.models import *


def index(request):
    return render(request, 'catalog/index.html')

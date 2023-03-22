from django.db.models import Count
from django.views.generic import ListView
from catalog.models import Product, Category
from django.contrib import messages
from django.shortcuts import redirect


class HomeView(ListView):
    model = Product
    template_name = 'home.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.annotate(cnt=Count('product'))
        context['best_products'] = Product.objects.filter(top_seller=True)
        return context


def signup_redirect(request):
    messages.error(request, "Something wrong here, it may be that you already have account!")
    return redirect('home')


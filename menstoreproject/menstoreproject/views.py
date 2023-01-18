from django.db.models import Count
from django.views.generic import ListView
from catalog.models import Product, Category


class HomeView(ListView):
    model = Product
    template_name = 'home.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.annotate(cnt=Count('product'))
        context['best_products'] = Product.objects.filter(top_seller=True)
        return context



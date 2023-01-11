from django.views.generic import ListView
from catalog.models import Product, Category


class HomeView(ListView):
    model = Product
    template_name = 'home.html'
    context_object_name = 'best_products'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Головна MenStore'
        context['categories'] = Category.objects.all()
        return context

    def get_queryset(self):
        return Product.objects.filter(top_seller=True).select_related('category')


from django.db.models import Count
from django.views.generic import ListView
from catalog.models import Product, Category
from .forms import ContactForm
from django.views.generic.edit import FormView
from django.contrib import messages


class HomeView(ListView):
    model = Product
    template_name = 'home.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.annotate(cnt=Count('product'))
        context['best_products'] = Product.objects.filter(top_seller=True)
        context['selected_products'] = Product.objects.filter(selected=True)
        return context


class ContactView(FormView):
    template_name = 'contact_us.html'
    form_class = ContactForm
    success_url = '/'

    def form_valid(self, form):
        form.send_email()
        messages.success(self.request, 'Дякуємо! Ваше повідомлення відправлено')
        return super().form_valid(form)

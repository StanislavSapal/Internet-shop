from django.views.generic import DetailView, TemplateView, CreateView, FormView
from .forms import OrderForm
from cart.models import Cart
from django.shortcuts import get_object_or_404, render
from django.db.models import F, Sum


class OrderConfirmationView(FormView, DetailView):
    form_class = OrderForm
    template_name = 'order/order_detail.html'
    success_url = 'done'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_object(self, queryset=None):
        return get_object_or_404(Cart, user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart_items'] = self.object.cartitem_set.all()
        context['total_cart_sum'] = self.object.cartitem_set.aggregate(price_total=Sum(F('product__price') *
                                                                                       F('quantity')))
        return context


def done(request):
    return render(request, 'order/done.html')

from django.views.generic import FormView
from .forms import OrderForm
from cart.models import Cart
from django.shortcuts import render
from django.db.models import F, Sum


class OrderConfirmationView(FormView):
    template_name = 'order/order_detail.html'
    form_class = OrderForm
    success_url = 'success'
    raise_exception = False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = Cart.objects.filter(user=self.request.user, status='O').last()
        context['cart'] = cart
        context['cart_items'] = cart.cartitem_set.all()
        context['total_cart_sum'] = cart.cartitem_set.aggregate(price_total=Sum(F('product__price') * F('quantity')))
        return context

    def form_valid(self, form):
        cart = Cart.objects.filter(user=self.request.user, status='O').last()
        form.save()
        cart.status = 'C'
        cart.save()
        return super(OrderConfirmationView, self).form_valid(form)


def successful_order_page_view(request):
    return render(request, 'order/successful_order.html')

from django.views.generic import FormView, ListView
from .forms import OrderForm
from cart.models import Cart
from django.shortcuts import render
from django.db.models import F, Sum
from django.contrib import messages
from .models import Order


class OrderConfirmationView(FormView):
    template_name = 'order/order_detail.html'
    form_class = OrderForm
    success_url = 'success'
    raise_exception = False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = self.request.cart
        context['cart'] = cart
        context['cart_items'] = cart.cartitem_set.all()
        context['total_cart_sum'] = cart.cartitem_set.aggregate(price_total=Sum(F('product__price') * F('quantity')))
        return context

    def form_valid(self, form):
        cart = self.request.cart
        form.save()
        cart.status = Cart.StatusChoices.closed
        cart.save()
        return super(OrderConfirmationView, self).form_valid(form)


def successful_order_page_view(request):
    messages.success(request, 'Замовлення прийнято')
    return render(request, 'order/successful_order.html')


class OrderList(ListView):
    model = Order
    template_name = 'order/user_orders.html'
    context_object_name = 'orders'

    def get_queryset(self):
        return Order.objects.filter(cart__user=self.request.user)

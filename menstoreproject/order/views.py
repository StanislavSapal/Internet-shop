from django.views.generic import FormView, ListView
from .forms import OrderForm
from cart.models import Cart
from django.shortcuts import render
from django.db.models import F, Sum
from django.contrib import messages
from .models import Order
from django.contrib.auth.mixins import LoginRequiredMixin
from .tasks import send_order_info_email_task


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
        if self.request.user.is_authenticated:
            order = Order.objects.filter(cart__user=self.request.user).last()
        else:
            order = Order.objects.filter(cart__token=self.request.session.token).last()
        order_info_message = f"Доброго дня, {order.first_name}. Ви зробили замовлення в магазині Menstore." \
                             f" Ваш номер замовлення {order.order_number}. Замовлення буде відправлене завтра. " \
                             f"Деталі за телефоном +380990288708"
        send_order_info_email_task.delay(
            order.email, order_info_message
        )
        return super(OrderConfirmationView, self).form_valid(form)


def successful_order_page_view(request):
    messages.success(request, 'Замовлення прийнято')
    return render(request, 'order/successful_order.html')


class OrderList(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'order/user_orders.html'
    context_object_name = 'orders'

    def get_queryset(self):
        return Order.objects.filter(cart__user=self.request.user).order_by('-created')

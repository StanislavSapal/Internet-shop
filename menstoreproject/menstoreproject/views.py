from django.db.models import Count
from django.views.generic import ListView
from catalog.models import Product, Category
from django.contrib import messages
from django.shortcuts import redirect
from django.http import HttpResponse
from django.urls import reverse
from allauth.account.views import (
    AjaxCapableProcessFormViewMixin,
    CloseableSignupMixin,
    RedirectAuthenticatedUserMixin,
)
from django.views.generic.edit import FormView


class HomeView(ListView):
    model = Product
    template_name = 'home.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        print('huj w zhopi')
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.annotate(cnt=Count('product'))
        context['best_products'] = Product.objects.filter(top_seller=True)
        return context


def signup_redirect_view(request):
    messages.error(request, "Something wrong here, it may be that you already have account!")
    return redirect('home')
    # message = 'redirect view works'
    # result = f'<h2> Attention {message} </h2>'
    # return HttpResponse(result)


class SignupView(RedirectAuthenticatedUserMixin,
                 CloseableSignupMixin,
                 AjaxCapableProcessFormViewMixin,
                 FormView):
    print('SignupView works in myviews')
    def form_invalid(self, form):
        """If the form is invalid, render the invalid form."""
        return redirect('home')


signup = SignupView.as_view()


def test_view(request):
    print('test_view works')
    messages.error(request, "Something wrong here, it may be that you already have account!")
    return redirect('signup_redirect')
    # message = 'redirect view works'
    # result = f'<h2> Attention {message} </h2>'
    # return HttpResponse(result)



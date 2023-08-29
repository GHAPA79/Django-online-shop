from django.shortcuts import render

from .forms import OrderForm


def create_order_view(request):
    return render(request, 'orders/order_create.html', context={
        'form': OrderForm(),
    })

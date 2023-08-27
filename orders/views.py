from django.shortcuts import render


def create_order_view(request):
    return render(request, 'orders/order_create.html')

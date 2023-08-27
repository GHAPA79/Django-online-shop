from django.urls import path

from .views import create_order_view

urlpatterns = [
    path('create/', create_order_view, name='order_create')
]

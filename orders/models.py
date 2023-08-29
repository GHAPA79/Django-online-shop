from django.db import models
from django.conf import settings
from django.utils.translation import gettext as _


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name=_('User'))
    is_paid = models.BooleanField(_('Is paid?'), default=False)

    first_name = models.CharField(_('First name'), max_length=100)
    last_name = models.CharField(_('Last name'), max_length=100)
    phone_number = models.CharField(_('Phone number'), max_length=15)
    address = models.CharField(_('Address'), max_length=700)

    order_notes = models.CharField(_('Order notes'), max_length=800, blank=True)

    datetime_created = models.DateTimeField(_('Date time created'), auto_now_add=True)
    datetime_modified = models.DateTimeField(_('date time modified'), auto_now=True)

    def __str__(self):
        return f'Order: {self.id}'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE, related_name='order_item')
    quantity = models.PositiveIntegerField(default=1)
    price = models.PositiveIntegerField()

    def __str__(self):
        return f'OrderItem: {self.id}: {self.product} x {self.quantity} (price:{self.price}'

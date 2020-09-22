from django.db import models
# from orders.models import order
from menu.models import Menu, Variation


class CartItem(models.Model):
    Cartt = models.ForeignKey('cart', on_delete=models.CASCADE, null=True, blank=True)
    products = models.ForeignKey(Menu, on_delete=models.CASCADE)
    variation = models.ManyToManyField(Variation)
    quantity = models.IntegerField(default=1)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    update = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        try:
            return str(self.id)
        except:
            return self.products.title

class cart(models.Model):
    # items = models.ManyToManyField(CartItem, null=True, blank=True)
    # product = models.ManyToManyField(Menu, null=True, blank=True)
    # order_id = models.ForeignKey(order, on_delete=models.CASCADE, null=True)
    total = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    update = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return "Cart id: %s" %(self.id)

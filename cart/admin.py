from django.contrib import admin

from .models import cart, CartItem
# Register your models here.

class CartAdmin(admin.ModelAdmin):
    list_display = ('id','timestamp')
    class Meta:
        model = cart

class CartItemAdmin(admin.ModelAdmin):
    list_display = ('id','Cartt','timestamp')

admin.site.register(cart, CartAdmin)

admin.site.register(CartItem, CartItemAdmin)
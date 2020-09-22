from django.contrib import admin

# Register your models here.

from .models import order

class OrderAdmin(admin.ModelAdmin):
    list_display = ('user','order_id','Cart','status','timestamp','updated','buktiPembayaran')
    date_hierarchy = ('updated')

admin.site.register(order, OrderAdmin)

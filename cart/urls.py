from django.urls import path
from django.conf.urls import url

from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.Cart, name='cart'),
    url(r'^(?P<category>[\w-]+)/(?P<slug>[\w-]+)/$', views.tambahKeranjang, name='updateCart'),
    url(r'^(?P<id>[\w-]+)/$', views.removeKeranjang, name='removeKeranjang'),  
]
from django.urls import path
from django.conf.urls import url

from . import views

app_name = 'orders'

urlpatterns = [
    path('', views.Checkout, name='Checkout'),
    path('upload-bukti/', views.uploadBukti, name='uploadBukti'),
    path("pesanan-masuk/", views.pesanan_masuk, name="pesananMasuk"),
    url(r'^(?P<id>[\w-]+)/$', views.selesaikanOrder, name='selesaikanOrder'),
    url(r'^(?P<id>[\w-]+)/(?P<user>[\w-]+)/$', views.lihatOrder, name='lihatOrder'),
    
]
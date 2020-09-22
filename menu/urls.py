from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'menu'

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^(?P<category>[\w_]+)/$', views.indexCategory, name='category'),
    url(r'^(?P<category>[\w_]+)/(?P<slug>[\w-]+)$', views.beli, name='produkSatuan'),  
]
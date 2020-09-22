from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from . import views, settings
from orders.views import orders, akun_lain
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    url(r'^result/$', views.cari, name="cari"),
    path('menu/', include('menu.urls')),
    path('registrasi/', views.registrasi, name="register"),
    path('logout/', views.user_logout, name="logout"),
    path('user_login/', views.user_login, name="user_login"),
    path('cart/', include('cart.urls')),
    path('checkout/', include('orders.urls')),
    path('akun/', orders, name='akun'),
    path('tester/', views.test, name='test'),
    url(r'^(?P<username>[\w-]+)/$', akun_lain, name='akunLain'),
    

    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
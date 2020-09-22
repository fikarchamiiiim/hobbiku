import time
from django.contrib.auth.decorators import login_required,user_passes_test
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from .models import order
from .utils import id_generatorOrder
from .forms import bukti_Pembayaran
from cart.models import cart, CartItem
from django.contrib.auth.models import User
from menu.models import Menu, Variation
# Create your views here.


def orders(request):
    profile = User.objects.select_related('userprofileinfo').get(id=request.user.id)
    orderan = order.objects.filter(user__id = request.user.id).order_by('-timestamp')

    context = {
        'profile':profile,
        'orderan':orderan,
    }
    template = 'orders/user.html'
    return render(request, template, context)

def akun_lain(request, username):
    profile = User.objects.select_related('userprofileinfo').get(username=username)
    orderan = order.objects.filter(user__id = request.user.id).order_by('-timestamp')

    context = {
        'profile':profile,
        'orderan':orderan,
    }
    template = 'orders/user.html'
    return render(request, template, context)


@login_required
def Checkout(request):
    try:
        the_id = request.session['cart_id']
        Cart = cart.objects.get(id=the_id)
    except:
        the_id = None
        return HttpResponseRedirect(reverse('cart:cart'))

    try:
        pesanan_baru = order.objects.get(Cart=Cart)
    except order.DoesNotExist:
        pesanan_baru = order()
        pesanan_baru.Cart = Cart
        pesanan_baru.user = request.user
        pesanan_baru.order_id = id_generatorOrder()
        pesanan_baru.save()
        del request.session['cart_id']
        del request.session['item_total']
    except:
        return HttpResponseRedirect(reverse('cart:cart'))
    
    orderan = order.objects.select_related('user','Cart').get(order_id=pesanan_baru.order_id)

    if pesanan_baru.status == "Selesai":
        # Cart.delete()
        del request.session['cart_id']
        del request.session['item_total']
        # del request.session['harga_total']
        return HttpResponseRedirect(reverse('cart:cart'))

    context = {
        'order_id': pesanan_baru.order_id,
        'orderan':orderan,
    }

    return render(request, 'orders/orders.html', context)


def uploadBukti(request):
    # model = buktiPembayaran
    uploaded = False
    id_transaksi = request.GET.get('idTrs')
    usrnm = request.GET.get('usrnm')
    if request.method == 'POST':
        form = bukti_Pembayaran(request.POST, request.FILES)
        uploaded_file = request.FILES['buktiPembayaran']
        fs = FileSystemStorage(location='media/bukti_pembayaran/')
        filename = fs.save(uploaded_file.name, uploaded_file)
        order_id = request.POST.get('order_id')
        user = request.POST.get('username')
        print(user)
        try:
            pesanan_masuk = order.objects.get(order_id = order_id,user__username=user)
            pesanan_masuk.buktiPembayaran = uploaded_file
            pesanan_masuk.save()
            uploaded = True
        except:
            Pesan = 'Username atau Id Transaksi tidak terdaftar'
        
    else:
        form = bukti_Pembayaran()
    context = {
        'pesan': 'Bukti pembayaran kamu berhasil di upload',
        'form': form,
        'uploaded': uploaded,
        'id_transaksi':id_transaksi,
        'usrnm':usrnm,
        # 'pesan':pesan,
    }
    template = 'orders/upload.html'
    return render(request, template, context)

@user_passes_test(lambda u: u.is_superuser)
def pesanan_masuk(request):
    orderan = order.objects.filter(status = 'Mulai').select_related('user','Cart').order_by('-timestamp')
    
    context = {
        'Orderan':orderan,
    }
    template = 'orders/pesanan_masuk.html'
    return render(request, template, context)

@user_passes_test(lambda u: u.is_superuser)
def selesaikanOrder(request, id):
    Order = order.objects.get(order_id=id)
    Order.status = ('Selesai')
    Order.save()

    return HttpResponseRedirect(reverse('orders:pesananMasuk'))

@user_passes_test(lambda u: u.is_superuser)
def lihatOrder(request, id, user):
    Order = order.objects.filter(order_id=id)
    cart_id = Order[0].Cart_id
    keranjang = CartItem.objects.select_related('Cartt','products').filter(Cartt_id = cart_id)
    total = keranjang[0].Cartt.total


    context = {
        'orderan' : Order,
        'keranjang' : keranjang,
        'total':total,
    }
    template = 'orders/detailOrder.html'
    return render(request, template, context)



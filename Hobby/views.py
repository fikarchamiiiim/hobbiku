from django.shortcuts import render
from django.db.models import Q
from django.contrib.auth.models import User
from menu.models import Category, Menu
from menu.forms import UserForm, UserProfileInfo
from orders.models import order

#login
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required,user_passes_test


def index(request):
    PesananMasuk = order.objects.filter(status = 'Mulai').count()
    carousel = Menu.objects.filter(diskon__gt=0).order_by('timestamp')[:2]
    produkBaru = Menu.objects.all().order_by('-timestamp')[:4]
    categories = Category.objects.all()
    request.session['JumlahPesanan'] = PesananMasuk
    context = {
        'title':'Hobbiku',
        'subtitle':'Selamat Datang di Hobbiku',
        'carousel':carousel,
        'Menu':produkBaru,
        'categories': categories,
    }

    return render(request, 'index.html', context)

def cari(request):
    # cari = Menu.objects.filter(judulMenu=inputCari)

    query = request.GET.get('cari')
    if query == 'semua':
        result = Menu.objects.filter(active=True,kuantitas__gt=0)
    else:
        result = Menu.objects.filter(Q(judulMenu__icontains=query) | Q(JK__icontains=query),active=True,kuantitas__gt=0)

    context = {
        'title':'Hasil Pencarian',
        'subtitle':'Hasil Pencarian',
        'Menus': result,
    }

    return render(request, 'menu/cari.html', context)

def PesananMasuk(request):
    PesananMasuk = order.objects.filter(buktiPembayaran__isnull = True)
    print('PesananMasuk')
    context = {
        'PesananMasuk':PesananMasuk,
    }
    return render(request, 'base.html', context)


def registrasi(request):

    #Set variable registered menjadi false
    registered = False

    #Jika methodnya POST, maka ambil data dari form kedalam maisng2 variable
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfo(data=request.POST)

        # Jika Valid maka save data dan encrypt password
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            # Set Variable Registered manjadi True
            registered = True

        else:
            print(user_form.errors,profile_form.errors)
    # Jika Salah, maka reload
    else:
        user_form = UserForm()
        profile_form = UserProfileInfo()
    
    return render(request, 'registrasi.html', {
                           'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Akun Tidak Ada")
        else:
            print("Ada yang mencoba masuk namun gagal!")
            print("Username : {} dan password : {}".format(username,password))
            return HttpResponseRedirect(reverse("user_login"))
    else:
        context = {
            "title" : "Login",
            "subtitle":"Login",
        }
    return render(request,'login.html', context)
    
def test(request):
    return render(request, 'unique_requests.html')
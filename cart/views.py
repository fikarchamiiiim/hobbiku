from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from menu.models import Menu, Variation
from .models import cart, CartItem
# Create your views here.


def Cart(request):
    try:
        the_id = request.session['cart_id']
        carts = cart.objects.get(id=the_id)
    except:
        the_id = None
    if the_id:
        new_total = 0
        for item in carts.cartitem_set.all():
            line_total = (item.products.hargaMenu - item.products.diskon) * item.quantity
            new_total += line_total
        # request.session['harga_total'] = line_total
        request.session['item_total'] = carts.cartitem_set.count()
        carts.total = new_total
        carts.save()
        context = {
            "cart": carts,
            'title': 'Keranjang',
            'subtitle': 'Keranjang',
        }
    else:
        empty_message = "Keranjang kamu masih kosong, Yuk belanja :)"
        context = {
            "empty": True,
            'title': 'Keranjang',
            'subtitle': 'Keranjang',
            'empty_message': empty_message,
        }

    template = "cart/view.html"
    return render(request, template, context)


def removeKeranjang(request, id):
    try:
        the_id = request.session['cart_id']
        carts = cart.objects.get(id=the_id)
    except:
        return HttpResponseRedirect(reverse('cart:cart'))
    cartitem = CartItem.objects.get(id=id)
    # cartitem.delete()
    cartitem.Cartt = None
    cartitem.save()

    return HttpResponseRedirect(reverse('cart:cart'))


def tambahKeranjang(request, category, slug):
    request.session.set_expiry(86400)

    try:
        the_id = request.session['cart_id']
    except:
        new_cart = cart()
        new_cart.save()
        request.session['cart_id'] = new_cart.id
        the_id = new_cart.id
    Cart = cart.objects.get(id=the_id)

    try:
        menu = Menu.objects.get(slug=slug)
    except Menu.DoesNotExist:
        pass
    except:
        pass

    variasiProduk = []
    if request.method == "POST":
        qty = request.POST['qty']
        for item in request.POST:
            key = item
            val = request.POST[key]
            try:
                v = Variation.objects.get(
                    product=menu, category__iexact=key, title__iexact=val)
                variasiProduk.append(v)
            except:
                pass

        cart_item = CartItem.objects.create(Cartt=Cart, products=menu)
        if len(variasiProduk) > 0:
            cart_item.variation.add(*variasiProduk)
        cart_item.quantity = qty
        cart_item.save()

        return HttpResponseRedirect(reverse('cart:cart'))

    return HttpResponseRedirect(reverse('cart:cart'))

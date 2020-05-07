from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

from cart.models import Cart

@login_required
def index(request):
    usercart = Cart.objects.all().filter(user_id=request.user.id)
    sumtotal = 0
    eachItem = {}
    for product in usercart:

        total = product.quantity * product.product.price
        eachItem[product.product.id] = total
        sumtotal += product.quantity * product.product.price
        rounded_sumtotal = ("{:.2f}".format(float(sumtotal)))

        context = {'carts': Cart.objects.all().filter(user_id=request.user.id), 'eachItemTotal': eachItem, 'sumTotal': rounded_sumtotal}
    return render(request, 'cart/index.html', context)


@csrf_exempt
def remove_cart_item(request, cartid):
    print(cartid)
    Cart.objects.filter(pk=cartid).delete()

    context = {'carts': Cart.objects.all().filter(user_id=request.user.id)}
    return render(request, 'cart/index.html', context)

def update_cart(request):
    #laga quantity þegar það er ýtt á + eða mínus og uppfæra þá total-ið
    pass


#def total_price(request):
#    total = sum([item.product.price for item in Cart.objects.all().filter(user_id=request.user.id)])
#    print(total)


from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

from cart.models import Cart
from order.models import Order


@login_required
def index(request):
    usercart = Cart.objects.all().filter(user_id=request.user.id)
    sumtotal = 0
    eachItem = {}
    for product in usercart:
        total = ("{:.2f}".format(float(product.quantity * product.product.price))+' $')
        eachItem[product.product.id] = total
        sumtotal += product.quantity * product.product.price
        rounded_sumtotal = ("{:.2f}".format(float(sumtotal))+' $')
        context = {'carts': Cart.objects.all().filter(user_id=request.user.id), 'eachItemTotal': eachItem, 'sumTotal': rounded_sumtotal}
    try:
        return render(request, 'cart/index.html', context)
    except:
        return render(request, 'cart/emptycart.html')


@csrf_exempt
def remove_cart_item(request, cartid):
    print(cartid)
    Cart.objects.filter(pk=cartid).delete()
    context = {'carts': Cart.objects.all().filter(user_id=request.user.id)}
    return render(request, 'cart/index.html', context)

def update_cart(request, cartid, quantity):
    print('in update cart')
    Cart.objects.filter(pk=cartid).update(quantity=quantity)
    context = {'carts': Cart.objects.all().filter(user_id=request.user.id)}
    return render(request, 'cart/index.html', context)


def create_order(request):
    if request.method == 'POST':
        print('we here')
        usercarts = Cart.objects.filter(user=request.user)
        for cart in usercarts:
            cart_total = 0
            cart_total += cart.product.price * cart.quantity
            Order.objects.create(user=cart.user, product=cart.product, quantity=cart.quantity, total=cart_total, processed=False)








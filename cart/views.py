from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
from cart.models import Cart
from order.models import Order

# Create your views here.

@login_required
def index(request):
    usercart = Cart.objects.all().filter(user_id=request.user.id, order_id__exact='').order_by('product__name')
    sumtotal = 0
    eachItem = {}
    for product in usercart:
        total = ("{:.2f}".format(float(product.quantity * product.product.price))+' $')
        eachItem[product.product.id] = total
        sumtotal += product.quantity * product.product.price
        rounded_sumtotal = ("{:.2f}".format(float(sumtotal))+' $')
        context = {'carts': usercart, 'eachItemTotal': eachItem, 'sumTotal': rounded_sumtotal}
    try:
        return render(request, 'cart/index.html', context)
    except:
        return render(request, 'cart/emptycart.html')


def remove_cart_item(request, cartid):
    if request.method == 'DELETE':
        print(cartid)
        Cart.objects.filter(pk=cartid).delete()
        return render(request, 'cart/index.html')


def update_cart(request, cartid, quantity):
    if request.method == 'PATCH':
        print('in update cart')
        Cart.objects.filter(pk=cartid).update(quantity=quantity)
        return render(request, 'cart/index.html')

# erum við að nota þetta???
def create_order(request):
    if request.method == 'POST':
        print('create_order: we here')
        usercarts = Cart.objects.filter(user=request.user)
        for cart in usercarts:
            cart_total = 0
            cart_total += cart.product.price * cart.quantity
            Order.objects.create(user=cart.user, product=cart.product, quantity=cart.quantity, total=cart_total, processed=False)


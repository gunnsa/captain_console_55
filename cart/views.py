from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from cart.models import Cart


@login_required
def index(request):
    """ Returns view of items in the current users cart """
    user_cart = Cart.objects.all().filter(user_id=request.user.id, order_id__exact='').order_by('product__name')
    sum_total = 0
    each_item = {}

    for product in user_cart:
        total = ("{:.2f}".format(float(product.quantity * product.product.price)) + ' $')
        each_item[product.product.id] = total
        sum_total += product.quantity * product.product.price
        rounded_sum_total = ("{:.2f}".format(float(sum_total)) + ' $')
        context = {'carts': user_cart, 'eachItemTotal': each_item, 'sumTotal': rounded_sum_total}

    if user_cart:
        return render(request, 'cart/index.html', context)
    else:
        return render(request, 'cart/emptycart.html')


def remove_cart_item(request, cartid):
    """ Removes product from the current users cart  """
    if request.method == 'DELETE':
        Cart.objects.filter(pk=cartid).delete()
        return render(request, 'cart/index.html')


def update_cart(request, cartid, quantity):
    """ Updates quantity of product in the current users cart """
    if request.method == 'PATCH':
        Cart.objects.filter(pk=cartid).update(quantity=quantity)
        return render(request, 'cart/index.html')


def remove_all_cart_items(request):
    print('in remove')
    """ Removes all products from the current users cart  """
    if request.method == 'DELETE':
        Cart.objects.filter(user=request.user.id, order_id='').delete()
        return render(request, 'cart/emptycart.html')

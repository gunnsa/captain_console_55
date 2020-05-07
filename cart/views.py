from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

from cart.models import Cart


def index(request):
    usercart = Cart.objects.all().filter(user_id=request.user.id)
    sumtotal = 0
    eachItem = []
    for product in usercart:
        print(product.quantity)
        total = product.quantity * product.product.price
        print('total: ', total)
        eachItem.append(total)
        sumtotal += product.quantity * product.product.price
        print(sumtotal)
        print('eachitem ', eachItem)
        #sum += carts.quantity * carts.product.price
        context = {'carts': Cart.objects.all().filter(user_id=request.user.id), 'sumtotal': sumtotal, 'eachitem': eachItem}
    return render(request, 'cart/index.html', context)

@csrf_exempt
def remove_cart_item(request, cartid):
    print(cartid)
    Cart.objects.filter(pk=cartid).delete()

    context = {'carts': Cart.objects.all().filter(user_id=request.user.id)}
    return render(request, 'cart/index.html', context)


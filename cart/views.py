from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

from cart.models import Cart


def index(request):
    total = sum([item.product.price for item in Cart.objects.all().filter(user_id=request.user.id)])
    context = {'carts': Cart.objects.all().filter(user_id=request.user.id), 'total': total}
    return render(request, 'cart/index.html', context)


@csrf_exempt
def remove_cart_item(request, cartid):
    print(cartid)
    Cart.objects.filter(pk=cartid).delete()

    context = {'carts': Cart.objects.all().filter(user_id=request.user.id)}
    return render(request, 'cart/index.html', context)


#def total_price(request):
#    total = sum([item.product.price for item in Cart.objects.all().filter(user_id=request.user.id)])
#    print(total)


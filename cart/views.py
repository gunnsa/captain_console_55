from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from cart.models import Cart
from product.models import Product


def index(request):
    context = {'carts': Cart.objects.all().filter(user_id=request.user.id)}
    return render(request, 'cart/index.html', context)


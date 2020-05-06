from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from cart.models import Cart


def index(request):
    context = {'carts': Cart.objects.all().filter(user_id=request.user.id)}
    return render(request, 'cart/index.html', context)

def remove_cart_item(request):
    #get all the items in the cart of the current user
    #remove the item from the users cart



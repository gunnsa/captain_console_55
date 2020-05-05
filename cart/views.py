from django.shortcuts import render
from cart.models import Cart


def index(request):
    context = {'cart': Cart.objects.all()}
    return render(request, 'cart/index.html', context)

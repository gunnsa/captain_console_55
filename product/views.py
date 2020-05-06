from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from cart.models import Cart
from product.models import Product


# Create your views here.
def index(request):
    if 'drop_filter' in request.GET:
        drop_filter = request.GET['drop_filter']
        products = [{
            'id': x.id,
            'name': x.name,
            'color': x.color,
            'price': x.price,
            'short_description': x.short_description,
            'manufacturer': x.manufacturer,

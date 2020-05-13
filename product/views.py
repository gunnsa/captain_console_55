import json

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import loader, RequestContext
from cart.models import Cart
from home.models import Newsletter
from product.models import Product
from wishlist.models import WishList

# Create your views here.

def index(request):
    if 'min_price' in request.GET:

        print('request: ', request) #request:  <WSGIRequest: GET '/products/?min_price=min&sort_by=min'>
        print('request: ', request.GET) #request: < QueryDict: {'min_price': ['min'], 'sort_by': ['min']} >



        products = JsonResponse_form(Product.objects.all().order_by('price'))
        return JsonResponse({'data': products})

    elif 'max_price' in request.GET:
        products = JsonResponse_form(Product.objects.all().order_by('-price'))
        return JsonResponse({'data': products})

    elif 'name' in request.GET:
        products = JsonResponse_form(Product.objects.all().order_by('name'))
        return JsonResponse({'data': products})

    elif 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        products = JsonResponse_form(Product.objects.filter(name__icontains=search_filter))
        return JsonResponse({'data': products})

    products = Product.objects.all().order_by('name')
    manufacturers = Product.objects.values_list("manufacturer", flat=True).distinct()

    context = {
        'products': products,
        'manufacturers': manufacturers,
    }
    return render(request, 'product/index.html', context)


# /products/id OG GEYMIR COOKIE
def get_product_by_id(request, id):
    product_id = id
    if request.method == 'GET':
        if id in request.COOKIES:
            product_id = request.COOKIES['id']
    elif request.method == 'POST':
        product_id = request.POST.get(id)

    all_products = Product.objects.all()

    response = render(request, 'product/product_details.html', {
        'product': get_object_or_404(Product, pk=id), 'all_products': all_products
    })
    response.set_cookie(str(id), product_id, max_age=604800)
    return response

    #return render(request, 'product/product_details.html', {
    #    'product': get_object_or_404(Product, pk=id)
    #})


def sort_product_by_specific(request, manufacturer):
    context = {'products': Product.objects.all()}
    return render(request, 'product/index.html', context)


def add_to_cart(request, productid, quantity):
    if request.method == 'POST':
        current_user = request.user.id
        if Cart.objects.filter(user_id__exact=current_user, product_id=productid, order_id__exact=''):
            existing_cart = Cart.objects.get(product_id=productid, user_id=current_user)
            existing_cart.quantity = existing_cart.quantity + quantity
            existing_cart.save()
        else:
            Cart.objects.create(user_id=current_user, product_id=productid, quantity=quantity)

    # context = {'products': Product.objects.all().order_by('name')}
    return render(request, 'product/index.html')


def add_to_wishlist(request, productid):
    if request.method == 'POST':
        current_user = request.user.id
        if WishList.objects.filter(user_id__exact=current_user, product_id=productid):
            existing_wishlist = WishList.objects.get(product_id=productid, user_id=current_user)
            existing_wishlist.save()
        else:
            WishList.objects.create(user_id=current_user, product_id=productid)

    # context = {'products': Product.objects.all().order_by('name')}
    return render(request, 'product/index.html')


def sort_by_brand(request, manufacturer):
    if 'min_price' in request.GET:
        #tilraun = JsonResponse_form(Product.objects.all().order_by('price'))
        #return JsonResponse({'data': tilraun})

        tilraun = JsonResponse_form(Product.objects.all().filter(manufacturer__exact=manufacturer).order_by('price'))
        return JsonResponse({'data': tilraun})

    elif 'max_price' in request.GET:
        tilraun = JsonResponse_form(Product.objects.all().filter(manufacturer__exact=manufacturer).order_by('-price'))
        return JsonResponse({'data': tilraun})

    elif 'name' in request.GET:
        tilraun = JsonResponse_form(Product.objects.all().filter(manufacturer__exact=manufacturer).order_by('name'))
        return JsonResponse({'data': tilraun})

    products = Product.objects.all().filter(manufacturer__exact=manufacturer)
    manufacturers = Product.objects.values_list("manufacturer", flat=True).distinct()

    context = {
        'products': products,
        'manufacturers': manufacturers,
    }
    return render(request, 'product/index.html', context)


def JsonResponse_form(request):
    products = [{
        'id': x.id,
        'name': x.name,
        'color': x.color,
        'price': x.price,
        'short_description': x.short_description,
        'manufacturer': x.manufacturer,
        'color': x.color,
        'firstImage': x.productimage_set.first().image
    } for x in request]
    return products


def add_to_newsletter(request, email):
    if request.method == 'POST':
        Newsletter.objects.create(email=email)
    return render(request, 'home/index.html')

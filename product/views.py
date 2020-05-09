from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from cart.models import Cart, CartTest
from product.models import Product
from user.models import User

# Create your views here.
def index(request):
    if 'brand_filter' in request.GET:
        drop_filter = request.GET['brand_filter']
        products = [{
            'id': x.id,
            'name': x.name,
            'color': x.color,
            'price': x.price,
            'short_description': x.short_description,
            'manufacturer': x.manufacturer,
            'color': x.color,
            'firstImage': x.productimage_set.first().image
        } for x in Product.objects.filter(manufacturer__exact=drop_filter)]
        return JsonResponse({'data': products})

    elif 'price' in request.GET:
        products = [{
            'id': x.id,
            'name': x.name,
            'color': x.color,
            'price': x.price,
            'short_description': x.short_description,
            'manufacturer': x.manufacturer,
            'color': x.color,
            'firstImage': x.productimage_set.first().image
        } for x in Product.objects.all().order_by('price')]
        return JsonResponse({'data': products})

    elif 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        products = [{
            'id': x.id,
            'name': x.name,
            'color': x.color,
            'price': x.price,
            'short_description': x.short_description,
            'manufacturer': x.manufacturer,
            'color': x.color,
            'firstImage': x.productimage_set.first().image
        } for x in Product.objects.filter(name__icontains=search_filter)]
        return JsonResponse({'data': products})

    products = Product.objects.all().order_by('name')
    manufacturers = Product.objects.values_list("manufacturer", flat=True).distinct()

    context = {
        'products': products,
        'manufacturers': manufacturers,
    }
    return render(request, 'product/index.html', context)

#/products/id
def get_product_by_id(request, id):

    product_id = id
    print(request.method)
    if request.method == 'GET':
        print(request.COOKIES)
        if id in request.COOKIES:
            product_id = request.COOKIES['id']
            print('GET-id: ' + request.COOKIES.get('id'))
    elif request.method == 'POST':
        product_id = request.POST.get(id)
        print('POST-id: ' + request.POST(id))

    response =  render(request, 'product/product_details.html', {
        'product': get_object_or_404(Product, pk=id)
    })

    response.set_cookie(str(id), product_id, max_age=10000)
    return response

    #return render(request, 'product/product_details.html', {
    #    'product': get_object_or_404(Product, pk=id)
    #})


def sort_product_by_specific(request, manufacturer):
    context = {'products': Product.objects.all()}
    return render(request, 'product/index.html', context)


#@login_required
@csrf_exempt
def add_to_cart(request, productid, quantity):
    if request.method == 'POST':
        current_user = request.user.id
        if Cart.objects.filter(user_id__exact=current_user, product_id=productid):
            existing_cart = Cart.objects.get(product_id=productid, user_id=current_user)
            print(existing_cart.quantity)
            existing_cart.quantity = existing_cart.quantity + quantity
            print(existing_cart.quantity)
            existing_cart.save()
        else:
            Cart.objects.create(user_id=current_user, product_id=productid, quantity=quantity)

    context = {'products': Product.objects.all().order_by('name')}
    return render(request, 'product/index.html', context)


def test_cookie(request, id):
    print(request.COOKIES)
    if request.COOKIES.get('id'):
        print(request.COOKIES['id'])
        return HttpResponse("Your product id is: {}".format(request.COOKIES['id']))

    else:
        print("Visiting for the first time.")
        response = HttpResponse("Visiting for the first time.")
        response.set_cookie('id', id, max_age=1000)
        return response

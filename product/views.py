from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
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
    return render(request, 'product/product_details.html', {
        'product': get_object_or_404(Product, pk=id)
    })


def sort_product_by_specific(request, manufacturer):
    context = {'products': Product.objects.all()}
    return render(request, 'product/index.html', context)


#@login_required
@csrf_exempt
def add_to_cart_geyma(request, productid, quantity):
    if request.method == 'POST':
        current_user = request.user.id
        if Cart.objects.filter(user_id__exact=current_user, product_id=productid):
            existing_cart = Cart.objects.get(product_id=productid, user_id=current_user)
            print(existing_cart.quantity)
            existing_cart.quantity = existing_cart.quantity + 1
            print(existing_cart.quantity)
            existing_cart.save()
        else:
            Cart.objects.create(user_id=current_user, product_id=productid, quantity=quantity)

    context = {'products': Product.objects.all().order_by('name')}
    return render(request, 'product/index.html', context)

@csrf_exempt
def add_to_cart(request, productid, quantity):
    if request.method == 'POST':
        current_user = request.user.id
        userproduct = Product.objects.filter(pk=productid)
        if CartTest.objects.filter(user_id=current_user):
            print('fundið')
            current_cart= CartTest.objects.get(user_id=current_user)
            product_to_add = Product()
            current_cart.product.add(userproduct)
        else:
            userinstance = User.objects.get(pk=current_user)
            instance = CartTest.objects.create(user=userinstance, quantity=quantity)
            instance.product.set(userproduct)
    context = {'products': Product.objects.all().order_by('name')}
    return render(request, 'product/index.html', context)



Yuji's answer is correct. You can not add an object to a M2M field until it has been saved. I wanted to mention a shorter way to create instances though.

user = User.objects.get(username=uname)
flst = FollowerList(follower=user) #use key word args to assign fields
flst.save()
flst.followed.add(user)
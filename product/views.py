from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from wishlist.models import WishList
from product.models import Product
from cart.models import Cart


def index(request):
    """ Returns selected 'Sort by' view """
    if 'min_price' in request.GET:
        products = json_response_form(Product.objects.all().order_by('price'))
        return JsonResponse({'data': products})

    elif 'max_price' in request.GET:
        products = json_response_form(Product.objects.all().order_by('-price'))
        return JsonResponse({'data': products})

    elif 'name' in request.GET:
        products = json_response_form(Product.objects.all().order_by('name'))
        return JsonResponse({'data': products})

    elif 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        products = json_response_form(Product.objects.filter(name__icontains=search_filter))
        return JsonResponse({'data': products})

    products = Product.objects.all().order_by('name')
    manufacturers = Product.objects.values_list("manufacturer", flat=True).distinct()

    context = {
        'products': products,
        'manufacturers': manufacturers,
    }
    return render(request, 'product/index.html', context)


def get_product_by_id(request, id):
    """ Returns display of chosen product and sets as well as gets COOKIES """
    product_id = id

    all_products = Product.objects.all()
    cookie_product_id = []
    for key, value in request.COOKIES.items():
        if value.isdigit():
            cookie_product_id.append(int(value))
    response = render(request, 'product/product_details.html', {
        'product': get_object_or_404(Product, pk=id), 'all_products': all_products,
        'cookie_product_id': cookie_product_id
    })
    response.set_cookie(str(id), product_id, max_age=432000)
    return response


def add_to_cart(request, productid, quantity):
    """ Adds product to current users cart """
    if request.method == 'POST':
        current_user = request.user.id

        if Cart.objects.filter(user_id__exact=current_user, product_id=productid, order_id__exact=''):
            existing_cart = Cart.objects.get(product_id=productid, user_id=current_user)
            existing_cart.quantity = existing_cart.quantity + quantity
            existing_cart.save()
        else:
            Cart.objects.create(user_id=current_user, product_id=productid, quantity=quantity)

    return render(request, 'product/index.html')


def add_to_wishlist(request, productid):
    """ Adds product to current users wishlist """
    if request.method == 'POST':
        current_user = request.user.id

        if WishList.objects.filter(user_id__exact=current_user, product_id=productid):
            existing_wishlist = WishList.objects.get(product_id=productid, user_id=current_user)
            existing_wishlist.save()
        else:
            WishList.objects.create(user_id=current_user, product_id=productid)

    return render(request, 'product/index.html')


def sort_by_brand(request, manufacturer):
    """ Returns either selected 'Filtered by' view or 'Filtered by' and 'Sort by' view """
    if 'min_price' in request.GET:
        product = json_response_form(Product.objects.all().filter(manufacturer__exact=manufacturer).order_by('price'))
        return JsonResponse({'data': product})

    elif 'max_price' in request.GET:
        product = json_response_form(Product.objects.all().filter(manufacturer__exact=manufacturer).order_by('-price'))
        return JsonResponse({'data': product})

    elif 'name' in request.GET:
        product = json_response_form(Product.objects.all().filter(manufacturer__exact=manufacturer).order_by('name'))
        return JsonResponse({'data': product})

    products = Product.objects.all().filter(manufacturer__exact=manufacturer)
    manufacturers = Product.objects.values_list("manufacturer", flat=True).distinct()

    context = {
        'products': products,
        'manufacturers': manufacturers,
    }
    return render(request, 'product/index.html', context)


def json_response_form(request):
    """ Helper function for 'Sort by' and 'Filter by' """
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

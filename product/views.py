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
            'description': x.description,
            'productImage': x.productimage_set.first().image
        } for x in Product.objects.filter(name_icontains=drop_filter)]
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

@csrf_exempt
def add_to_cart(request, productid):
    current_user = request.user.id
    Cart.objects.create(user_id=current_user, product_id=productid, quantity=1)
    context = {'products': Product.objects.all().order_by('name')}
    return render(request, 'product/index.html', context)




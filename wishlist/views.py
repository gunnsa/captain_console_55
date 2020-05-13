from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from cart.models import Cart
from wishlist.models import WishList


@login_required
def index(request):
    wishlist = WishList.objects.all().filter(user_id=request.user.id).order_by('product__name')
    context = {'wishlist': wishlist}
    try:
        return render(request, 'wishlist/index.html', context)

    except:
        return render(request, 'wishlist/emptywishlist.html')


def remove_wishlist_item(request, wishlistid):
    if request.method == 'DELETE':
        print(wishlistid)
        WishList.objects.filter(pk=wishlistid).delete()
        return render(request, 'wishlist/index.html')


@csrf_exempt
def add_to_cart(request, productid):
    if request.method == 'POST':
        current_user = request.user.id
        if Cart.objects.filter(user_id__exact=current_user, product_id=productid, order_id__exact=''):
            existing_cart = Cart.objects.get(product_id=productid, user_id=current_user)
            existing_cart.quantity = existing_cart.quantity + 1
            existing_cart.save()
        else:
            Cart.objects.create(user_id=current_user, product_id=productid, quantity=1)

    WishList.objects.filter(user_id__exact=current_user, product_id=productid).delete()
    # context = {'products': Product.objects.all().order_by('name')}
    return render(request, 'wishlist/index.html')

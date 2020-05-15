from django.contrib.auth.decorators import login_required
from wishlist.models import WishList
from django.shortcuts import render
from cart.models import Cart


@login_required
def index(request):
    """ Returns view of current users wishlist """
    wishlist = WishList.objects.all().filter(user_id=request.user.id).order_by('product__name')
    context = {'wishlist': wishlist}

    if wishlist:
        return render(request, 'wishlist/index.html', context)
    else:
        return render(request, 'wishlist/emptywishlist.html')


def remove_wishlist_item(request, wishlistid):
    """ Removes product from current users wishlist """
    if request.method == 'DELETE':
        WishList.objects.filter(pk=wishlistid).delete()
        return render(request, 'wishlist/index.html')


def add_to_cart(request, productid):
    """ Moves product from current users wishlist to cart """
    if request.method == 'POST':
        print('1')
        current_user = request.user.id

        if Cart.objects.filter(user_id__exact=current_user, product_id=productid, order_id__exact=''):
            print('2')
            existing_cart = Cart.objects.get(product_id=productid, user_id=current_user,order_id__exact='')
            existing_cart.quantity = existing_cart.quantity + 1
            existing_cart.save()
        else:
            Cart.objects.create(user_id=current_user, product_id=productid, quantity=1)

    WishList.objects.filter(user_id__exact=current_user, product_id=productid).delete()
    return render(request, 'wishlist/index.html')

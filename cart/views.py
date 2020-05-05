from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from cart.models import Cart
from product.models import Product


def index(request):
    context = {'cart': Cart.objects.all()}
    return render(request, 'cart/index.html', context)



#def add_to_cart(request, id):
 #   product = get_object_or_404(Product, pk=id)
  #  cart, created = Cart.objects.get_or_create(user=request.user, active=True)
   # #order, created = BookOrder.objects.get_or_create(book=book, cart=cart)
    #cart.quantity += 1
    #cart.save()
    #messages.success(request, "Cart updated!")
    #return render(request, 'cart/index.html')



def add_to_cart(request, slug):
    cart=Cart.objects.all()
    try:
        product = Product.objects.get(slug=slug)
    except Product.DoesNotExist:
        pass
    except:
        pass
    if product not in cart.products.all():
        cart.products.add(product)
    else:
        cart.products.remove(product)
        return HttpResponseRedirect("/cart/")

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.


@login_required
def index(request):
    usercart = Cart.objects.all().filter(user_id=request.user.id, order_id__exact='').order_by('product__name')
    sumtotal = 0
    eachItem = {}
    for product in usercart:
        total = ("{:.2f}".format(float(product.quantity * product.product.price))+' $')
        eachItem[product.product.id] = total
        sumtotal += product.quantity * product.product.price
        rounded_sumtotal = ("{:.2f}".format(float(sumtotal))+' $')
        context = {'carts': usercart, 'eachItemTotal': eachItem, 'sumTotal': rounded_sumtotal}
    try:
        return render(request, 'cart/index.html', context)
    except:
        return render(request, 'cart/emptycart.html')
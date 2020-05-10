from django.shortcuts import render, redirect

from cart.models import Cart
from order.forms.delivery_form import DeliveryForm
from order.models import ContactInformation, Order


def order_contact_form(request):
    delivery = ContactInformation.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = DeliveryForm(instance=delivery, data=request.POST)
        if form.is_valid():
            delivery = form.save(commit=False)
            delivery.user = request.user
            delivery.save()
            usercart = Cart.objects.filter(user_id=request.user)
            for item in usercart:
                sumtotal = item.product.price * item.quantity
            order = Order.objects.create(total=sumtotal)
            order.line_items.set(usercart)
            return redirect('contactinfo-index')
    return render(request, 'order/contactinfo.html', {
        'form': DeliveryForm(instance=delivery)
    })


def get_payment(request):
    #get payment info
    pass

def processed_order(request):
    #skrifa niður í gagnagrunn nýtt instance af processed order
    #setja current order á núverandi order í false
    pass

def create_order(request):
    item_list = []
    if '/order/delivery' in request.POST :
        usercart = Cart.objects.filter(user_id=request.user)
        for item in usercart:
            sumtotal = item.product.price * item.quantity
            item_list.append(item)
        Order.objects.create(line_items=item_list, total=sumtotal)
        return redirect('contactinfo-index')
    return render(request, 'order/contactinfo.html', {
        'form': DeliveryForm(instance=create_order)
    })

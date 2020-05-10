from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from cart.models import Cart
from order.forms.delivery_form import DeliveryForm
from order.forms.payment_form import PaymentForm
from order.models import ContactInformation, Order, Payment


def order_contact_form(request):
    delivery = ContactInformation.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = DeliveryForm(instance=delivery, data=request.POST)
        if form.is_valid():
            delivery = form.save(commit=False)
            delivery.user = request.user
            delivery.save()
            return redirect('payment-index')

    return render(request, 'order/contactinfo.html', {
        'form': DeliveryForm(instance=delivery)
    })


def get_payment(request):
    payment = Payment.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = DeliveryForm(instance=payment, data=request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.authorized = True   #bara athuga
            payment.save()
            return redirect('payment-index') #geyma

    return render(request, 'order/payment.html', {
        'form': PaymentForm(instance=payment)
    })


def processed_order(request):
    #skrifa niður í gagnagrunn nýtt instance af processed order
    #setja current order á núverandi order í false
    pass


@csrf_exempt
def create_order(request):
    if request.method == 'POST':
        print('we here')
        usercarts = Cart.objects.filter(user=request.user)
        for cart in usercarts:
            cart_total = 0
            cart_total += cart.product.price * cart.quantity
            Order.objects.create(user=cart.user, product=cart.product, quantity=cart.quantity, total=cart_total, processed=False)
        return redirect('contactinfo-index')


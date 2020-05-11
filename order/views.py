from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from cart.models import Cart
from order.forms.contact_form import ContactForm
from order.forms.payment_form import PaymentForm
from order.models import ContactInformation, Order, Payment


def order_contact_form(request):
    print('1')
    delivery = ContactInformation.objects.filter(user=request.user).first()
    if request.method == 'POST':
        print('2')
        form = ContactForm(instance=delivery, data=request.POST)
        if form.is_valid():
            print('3')
            delivery = form.save(commit=False)
            delivery.user = request.user
            delivery.save()
            return redirect('payment-index')

    return render(request, 'order/contactinfo.html', {
        'form': ContactForm(instance=delivery)
    })


def get_payment(request):
    print('inside')
    payment = Payment.objects.filter(user=request.user).first()
    if request.method == 'POST':
        print('wayyyyy inside')
        form = PaymentForm(instance=payment, data=request.POST)
        if form.is_valid():
            print('wayyyyy inside 2')
            payment = form.save(commit=False)
            payment.user = request.user
            payment.save()
            return redirect('displayorder-index') #PASSIVE AGRESSIVE SERIOUSLY HER ER REDIRECT

    return render(request, 'order/payment.html', {
        'form': PaymentForm(instance=payment)
    })


def create_order(request):
    if request.method == 'POST':
        usercarts = Cart.objects.filter(user=request.user)
        for cart in usercarts:
            cart_total = 0
            cart_total += cart.product.price * cart.quantity
            Order.objects.create(user=cart.user, product=cart.product, quantity=cart.quantity, total=cart_total, processed=False)
        return redirect('contactinfo-index')



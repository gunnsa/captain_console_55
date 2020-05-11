from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from cart.models import Cart
from order.forms.delivery_form import DeliveryForm
from order.forms.payment_form import PaymentForm
from order.models import ContactInformation, Order, Payment, ProcessedOrder


def order_contact_form(request):
    print('1')
    delivery = ContactInformation.objects.filter(user=request.user).first()
    if request.method == 'POST':
        print('2')
        form = DeliveryForm(instance=delivery, data=request.POST)
        if form.is_valid():
            print('3')
            delivery = form.save(commit=False)
            delivery.user = request.user
            delivery.save()
            return redirect('payment-index')

    return render(request, 'order/contactinfo.html', {
        'form': DeliveryForm(instance=delivery)
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
            payment.authorized = True   #bara athuga
            payment.save()
            return redirect('displayorder-index') #PASSIVE AGRESSIVE SERIOUSLY HER ER REDIRECT

    return render(request, 'order/payment.html', {
        'form': PaymentForm(instance=payment)
    })


@csrf_exempt
def create_order(request):
    if request.method == 'POST':
        usercarts = Cart.objects.filter(user=request.user)
        for cart in usercarts:
            cart_total = 0
            cart_total += cart.product.price * cart.quantity
            Order.objects.create(user=cart.user, product=cart.product, quantity=cart.quantity, total=cart_total, processed=False)
        return redirect('contactinfo-index')


@csrf_exempt
def processed_order(request):
    #skrifa niður í gagnagrunn nýtt instance af processed order

    if request.method == 'POST':
        print('we here')
        userorder = Order.objects.filter(user=request.user)
        contact_info = ContactInformation.objects.get(user=request.user)
        payment_info = Payment.objects.get(user=request.user)

        sum_total = 0
        for order in userorder:
            print('ORDER: ', order)
            sum_total += order.product.price * order.quantity

        instance = ProcessedOrder.objects.create(user_id=request.user.id, contact_info=contact_info, payment_info=payment_info, sum_total=sum_total, confirmed=False)
        instance.line_items.set(userorder)

    return redirect(request, 'displayorder-index')




def display_order(request):
    tilraun = ProcessedOrder.objects.filter(user_id=request.user.id)

    print(tilraun)

    order = ProcessedOrder.objects.filter(user=request.user)
    print(order)
    for item in order:
        print(item)

    return render(request, 'order/display_order.html')


    usercart = Cart.objects.all().filter(user_id=request.user.id)
    sumtotal = 0
    eachItem = {}
    for product in usercart:
        total = product.quantity * product.product.price
        eachItem[product.product.id] = total
        sumtotal += product.quantity * product.product.price
        rounded_sumtotal = ("{:.2f}".format(float(sumtotal)))
        context = {'carts': Cart.objects.all().filter(user_id=request.user.id), 'eachItemTotal': eachItem, 'sumTotal': rounded_sumtotal}
    try:
        return render(request, 'cart/index.html', context)
    except:
        return render(request, 'cart/emptycart.html')

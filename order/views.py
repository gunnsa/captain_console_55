from django.shortcuts import render, redirect
from cart.models import Cart
from order.forms.contact_form import ContactForm
from order.forms.payment_form import PaymentForm
from order.models import ContactInformation, Order, Payment

# Create your views here.

def order_contact_form(request):
    ''' þegar ýtir á 'proceed to next step' í cart
        - sendir fyrst hingað með GET request og skilar 'ContactForm'
        - fyllir út upplýsingar og ýtir á 'Continue to payment' þá fer hann aftur inn í fallið með POST request og
            ef formið er valid þá vistar hann upplýsingarnar í db og redirectar á 'payment-index' '''

    contact_info = ContactInformation.objects.filter(user=request.user).first()

    if request.method == 'POST':
        form = ContactForm(instance=contact_info, data=request.POST)
        if form.is_valid():

            contact_info = form.save(commit=False)
            contact_info.user = request.user
            contact_info.save()
            return redirect('payment-index')


    return render(request, 'order/contactinfo.html', {
        'form': ContactForm(instance=contact_info)
    })


def get_payment(request):
    ''' þegar ýtir á 'Continue to payment' í contactInfo.html
            - sendir fyrst hingað með GET request og skilar 'PaymentForm'
            - fyllir út upplýsingar og ýtir á 'Continue to payment' þá fer hann aftur inn í fallið með POST request og
                ef formið er valid þá vistar hann upplýsingarnar í db og redirectar á 'createorder-index' '''
    print('get_payment: 1')
    payment = Payment.objects.filter(user=request.user).first()
    if request.method == 'POST':
        print('get_payment: 2')
        form = PaymentForm(instance=payment, data=request.POST)
        if form.is_valid():
            print('get_payment: 3 -- form.is_valid()')
            payment = form.save(commit=False)
            payment.user = request.user
            payment.save()
            return redirect('displayorder-index')  # PASSIVE AGRESSIVE SERIOUSLY HER ER REDIRECT
        else:
            print('FORM INVALID')
    return render(request, 'order/payment.html', {
        'form': PaymentForm(instance=payment)
    })


def display_order(request):
    usercart = Cart.objects.all().filter(user_id=request.user.id, order_id__exact='')
    userinfo = ContactInformation.objects.filter(user_id=request.user.id)
    sumtotal = 0
    eachItem = {}
    print('display_order')
    for product in usercart:
        total = ("{:.2f}".format(float(product.quantity * product.product.price))+' $')
        eachItem[product.product.id] = total
        sumtotal += product.quantity * product.product.price
        rounded_sumtotal = ("{:.2f}".format(float(sumtotal))+' $')
        context = {'carts': usercart, 'eachItemTotal': eachItem, 'sumTotal': rounded_sumtotal, 'info': userinfo}
    return render(request, 'order/display_order.html', context)


# þegar ýtt er á 'proceed to next step'
def create_order(request):

    if request.method == 'POST':
        current_user = request.user
        payment_info = Payment.objects.get(user_id=current_user)
        contact_info = ContactInformation.objects.get(user_id=current_user)

        instance = Order.objects.create(user=current_user, payment_info=payment_info, contact_info=contact_info, processed=True)
        user_cart = Cart.objects.filter(user=current_user, order_id__exact='')

        for user in user_cart:
            instance.cart.add(user)
            user_cart.update(order_id=instance.id)
        return render(request, 'order/display_order.html')


def overview(request):
        useroder = Order.objects.filter(user_id=request.user.id).order_by('-id')[0]
        usercart = Cart.objects.filter(user_id=request.user.id, order_id__exact=useroder.id)
        userinfo = ContactInformation.objects.filter(user_id=request.user.id)
        sumtotal = 0
        eachItem = {}
        print('display_order')
        for product in usercart:
            total = ("{:.2f}".format(float(product.quantity * product.product.price)) + ' $')
            eachItem[product.product.id] = total
            sumtotal += product.quantity * product.product.price
            rounded_sumtotal = ("{:.2f}".format(float(sumtotal)) + ' $')
            context = {'carts': usercart, 'eachItemTotal': eachItem, 'sumTotal': rounded_sumtotal, 'info': userinfo}
        return render(request, 'order/overview_order.html', context)



#tengt overview_order.html, síðan sem á að birtast eftir að þú staðfestir pöntunina, ss gerist eftir display_order.html


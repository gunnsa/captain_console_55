from django.forms import forms

from order.models import ContactInformation, Order, Payment
from order.forms.contact_form import ContactForm
from order.forms.payment_form import PaymentForm
from django.shortcuts import render, redirect
from cart.models import Cart


def order_contact_form(request):
    """ Returns Contact information form and saves current users input to database """
    contact_info = ContactInformation.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = ContactForm(instance=contact_info, data=request.POST)
        if form.is_valid():
            contact_info = form.save(commit=False)
            contact_info.user = request.user
            contact_info.save()
            return redirect('payment-index')
        else:
            print(form.errors)
            error = form.errors
            return render(request, 'order/contact_info.html', {
                'form': ContactForm(instance=contact_info),
                'error': error
            })
    else:
        return render(request, 'order/contact_info.html', {
            'form': ContactForm(instance=contact_info)
        })


def get_payment(request):
    """ Returns Payment information form and saves current users input to database """
    payment = Payment.objects.filter(user=request.user).first()

    if request.method == 'POST':
        form = PaymentForm(instance=payment, data=request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.user = request.user
            payment.save()
            return redirect('displayorder-index')
        else:
            print(form.errors)
            error = form.errors
            return render(request, 'order/payment.html', {
                'form': PaymentForm(instance=payment),
                'error': error
            })

    return render(request, 'order/payment.html', {
        'form': PaymentForm(instance=payment)
    })


def display_order(request):
    """ Returns read only view of all information regarding current users order """
    user_cart = Cart.objects.all().filter(user_id=request.user.id, order_id__exact='')
    user_info = ContactInformation.objects.filter(user_id=request.user.id)
    sum_total = 0
    each_item = {}

    for product in user_cart:
        total = ("{:.2f}".format(float(product.quantity * product.product.price))+' $')
        each_item[product.product.id] = total
        sum_total += product.quantity * product.product.price
        rounded_sum_total = ("{:.2f}".format(float(sum_total))+' $')
        context = {'carts': user_cart, 'eachItemTotal': each_item, 'sumTotal': rounded_sum_total, 'info': user_info}

    return render(request, 'order/display_order.html', context)


def create_order(request):
    """ Creates instance of order from given information and users current cart """
    if request.method == 'POST':
        current_user = request.user
        payment_info = Payment.objects.get(user_id=current_user)
        contact_info = ContactInformation.objects.get(user_id=current_user)
        instance = Order.objects.create(
            user=current_user, payment_info=payment_info, contact_info=contact_info, processed=True)
        user_cart = Cart.objects.filter(user=current_user, order_id__exact='')

        for user in user_cart:
            instance.cart.add(user)
            user_cart.update(order_id=instance.id)

        return render(request, 'order/display_order.html')


def overview(request):
    """ Returns view of processed and confirmed order """
    user_order = Order.objects.filter(user_id=request.user.id).order_by('-id')[0]
    user_cart = Cart.objects.filter(user_id=request.user.id, order_id__exact=user_order.id)
    user_info = ContactInformation.objects.filter(user_id=request.user.id)
    sum_total = 0
    each_item = {}

    for product in user_cart:
        total = ("{:.2f}".format(float(product.quantity * product.product.price)) + ' $')
        each_item[product.product.id] = total
        sum_total += product.quantity * product.product.price
        rounded_sumtotal = ("{:.2f}".format(float(sum_total)) + ' $')
        context = {'carts': user_cart, 'eachItemTotal': each_item, 'sumTotal': rounded_sumtotal, 'info': user_info}

    return render(request, 'order/overview_order.html', context)


def order_history(request):
    """ Returns view of current users order history """

    user_info = ContactInformation.objects.filter(user_id=request.user.id)
    user_order = Order.objects.all().filter(user_id=request.user.id)

    sum_total = 0
    each_item = {}
    each_order = {}

    for cart in user_order:
        for product in cart.cart.all():
            total = ("{:.2f}".format(float(product.quantity * product.product.price)) + ' $')
            each_item[product.id] = total

            sum_total += product.quantity * product.product.price
            rounded_sum_total = ("{:.2f}".format(float(sum_total)) + ' $')

        each_order[cart.id] = rounded_sum_total
        sum_total = 0

        context = {'user_order': user_order, 'info': user_info, 'eachItemTotal': each_item, 'sumTotal': each_order}

    return render(request, 'order/order_history.html', context)

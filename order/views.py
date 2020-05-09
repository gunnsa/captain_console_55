from django.shortcuts import render, redirect

from order.forms.delivery_form import DeliveryForm
from order.models import ContactInformation


def order_contact_form(request):
    delivery = ContactInformation.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = DeliveryForm(instance=delivery, data=request.POST)
        if form.is_valid():
            delivery = form.save(commit=False)
            delivery.user = request.user
            delivery.save()
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

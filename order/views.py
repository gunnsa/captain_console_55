from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


# Create your views here.
from order.models import Delivery


def delivery_form(request):
    if request.method == 'GET':
      form = UserCreationForm(data=request.POST)
      if form.is_valid():
          form.save()
          return redirect('delivery-index')
    return render(request, 'order/delivery.html', {
        'form': UserCreationForm()
    })

def delivery(request):
    delivery = Delivery.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = DeliveryForm(instance=delivery, data=request.POST)
        if form.is_valid():
            delivery = form.save(commit=False)
            delivery.user = request.user
            delivery.save()
            return redirect('delivery-index')
    return render(request, 'user/delivery.html', {
        'form': DeliveryForm(instance=delivery)
    })
def get_payment(request):
    #get payment info
    pass

def processed_order(request):
    #skrifa niður í gagnagrunn nýtt instance af processed order
    #setja current order á núverandi order í false
    pass

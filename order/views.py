from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    if request.method == 'GET':
      form = UserCreationForm(data=request.POST)
      if form.is_valid():
          form.save()
          return redirect('delivery-index')
    return render(request, 'order/delivery.html', {
        'form': UserCreationForm()
    })
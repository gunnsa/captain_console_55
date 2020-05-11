from django.urls import path
from . import views


urlpatterns = [
    #http://localhost:8000/order
    path('', views.order_contact_form, name="contactinfo-index"),
    path('create', views.create_order),
    path('payment', views.get_payment, name="payment-index"),
    path('payment/create', views.processed_order, name="prodessed-order"),
    path('display_order', views.display_order, name="displayorder-index")
]

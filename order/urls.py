from django.urls import path
from . import views


urlpatterns = [
    #http://localhost:8000/
    path('', views.order_contact_form, name="contactinfo-index"),
    path('create', views.create_order),
    path('payment', views.get_payment, name="payment-index"),
    path('<int:orderId>', views.processed_order, name="prodessed-order"),
]

from django.urls import path
from . import views


urlpatterns = [
    # http://localhost:8000/order
    path('', views.order_contact_form, name="contactinfo-index"),
    path('payment', views.get_payment, name="payment-index"),
    path('displayorder/create', views.create_order, name="createorder-index"),
    path('displayorder', views.display_order, name="displayorder-index"),
    path('overview', views.overview, name="overview-index")
]

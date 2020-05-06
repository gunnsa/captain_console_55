from django.urls import path
from . import views
from .views import add_to_cart

urlpatterns = [
    #http://localhost:8000/cart
    path('', views.index, name="cart-index"),
    #path('', add_to_cart, name="cart")
]

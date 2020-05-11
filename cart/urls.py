from django.urls import path
from . import views

urlpatterns = [
    #http://localhost:8000/cart
    path('', views.index, name="cart-index"),
    path('<int:cartid>/remove_cart_item', views.remove_cart_item),

    #path('create', views.create_order)
    #path('', add_to_cart, name="cart")
]

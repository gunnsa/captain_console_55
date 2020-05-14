from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/cart
    path('', views.index, name="cart-index"),
    path('<int:cartid>/remove_cart_item', views.remove_cart_item),
    path('<int:cartid>/update_cart/<int:quantity>', views.update_cart),
    path('remove_all_cart_items/', views.remove_all_cart_items)
]

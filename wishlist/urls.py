from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/wishlist
    path('', views.index, name="wishlist-index"),
    path('<int:cartid>/remove_cart_item', views.remove_cart_item),
    path('<int:cartid>/update_cart/<int:quantity>', views.update_cart)
]

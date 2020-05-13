from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/wishlist
    path('', views.index, name="wishlist-index"),
    path('<int:wishlistid>/remove_wishlist_item', views.remove_wishlist_item),
    path('<int:productid>/add_to_cart/', views.add_to_cart),
]

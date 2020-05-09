from django.urls import path
from . import views

urlpatterns = [
    #http://localhost:8000/product
    path('', views.index, name="products-index"),
    path('<int:id>', views.get_product_by_id, name="product-details"),
    path('<int:productid>/add_to_cart/<int:quantity>', views.add_to_cart)
    #path('<int:productid>/add_to_cart_test/<int:quantity>', views.add_to_cart_test),
    #path('?search_filter=<str:searchText>',views.search ,name="product-search")
    #path('price=<int:searchtext>', views.sort_product_by_price)
    #path('cart', add_to_cart, name="cart")
]

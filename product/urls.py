from django.urls import path
from . import views

urlpatterns = [
    #http://localhost:8000/product
    path('', views.index, name="products-index"),
    path('<int:id>', views.get_product_by_id, name="product-details")
]

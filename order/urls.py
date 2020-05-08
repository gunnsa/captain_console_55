from django.urls import path
from . import views

urlpatterns = [
    #http://localhost:8000/
    path('delivery', views.index, name="delivery-index")
]

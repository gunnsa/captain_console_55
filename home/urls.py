from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/
    path('', views.index, name="home-index"),
    path('add_to_newsletter/<str:email>', views.add_to_newsletter)
]

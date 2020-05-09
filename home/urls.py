from django.urls import path
from . import views

urlpatterns = [
    #http://localhost:8000/
    path('', views.index, name="home-index"),
    path('test_cookie/', views.test_cookie, name='test_cookie')
]

from django.db import models
from django.contrib.auth.models import User

from cart.models import Cart
from product.models import Product
#from django_countries.fields import CountryField

class Delivery(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    email_address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=7)
    home_address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CountryField()
    #country = CountryField(blank_label='(select country)')
    zip_code = models.CharField(max_length=3)
    additional_info = models.CharField(max_length=999, blank=True)

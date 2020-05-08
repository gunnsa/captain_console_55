from django.contrib.auth.models import User
from django.db import models
from product.models import Product


class Cart(models.Model):
    user = models.ForeignKey(User, blank=True, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()


class Delivery(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    email_address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=7)
    home_address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=3)
    additional_info = models.CharField(max_length=999)
    order_date = models.DateTimeField()


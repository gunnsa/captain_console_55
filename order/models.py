from django.contrib.auth.models import User
from django.db import models

from cart.models import Cart
from product.models import Product


# Create your models here.


class Order(models.Model):
    order = models.ManyToManyField(Cart, on_delete=models.CASCADE)
    current_order = models.BooleanField()
    order_date = models.DateTimeField()



class Delivery(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    email_address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=7)
    home_address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=3)
    additional_info = models.CharField(max_length=999)


class PickUp(models.Model):
    pickup_instore = models.BooleanField()


class Payment(models.Model):
    pass


class ProcessedOrder(models.Model):
    delivery_id = models.OneToOneField(Delivery, blank=True,on_delete=models.CASCADE)
    pickup_id = models.OneToOneField(PickUp, blank=True,on_delete=models.CASCADE)
    payment_id = models.OneToOneField(Payment, on_delete=models.CASCADE)
    orders = models.OneToOneField(Order, on_delete=models.CASCADE)

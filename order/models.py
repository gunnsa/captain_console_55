from django.db import models
from django.contrib.auth.models import User
from cart.models import Cart
from product.models import Product
from django_countries.fields import CountryField


class ContactInformation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    email_address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=7)
    home_address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = CountryField(blank_label='(Select country)')
    zip_code = models.CharField(max_length=3)
    home_delivery = models.BooleanField()
    additional_info = models.CharField(max_length=999, blank=True)
    current = models.BooleanField(default=True)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total = models.FloatField()
    processed = models.BooleanField()

class Payment(models.Model):
    card_number = models.PositiveIntegerField()
    card_month = models.PositiveIntegerField()
    card_year = models.PositiveIntegerField()
    card_CVC = models.PositiveIntegerField()
    current = models.BooleanField(default=True)
    authorized = models.BooleanField()

class ProcessedOrder(models.Model):
    line_items = models.ManyToManyField(Order)
    contact_info = models.ForeignKey(ContactInformation, on_delete=models.CASCADE)
    payment_info = models.ForeignKey(Payment, on_delete=models.CASCADE)
    sum_total = models.FloatField()




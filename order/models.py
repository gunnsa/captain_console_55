from django.core.validators import RegexValidator, MinLengthValidator
from django_countries.fields import CountryField
from django.contrib.auth.models import User
from product.models import Product
from datetime import datetime
from django.db import models
from cart.models import Cart


class ContactInformation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    email_address = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=7, validators=[RegexValidator('^[0-9]*$'), MinLengthValidator(7)])
    home_address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = CountryField(blank_label='(Select country)')
    zip_code = models.CharField(max_length=3, validators=[RegexValidator('^[0-9]*$'), MinLengthValidator(3)])
    additional_info = models.CharField(max_length=999, blank=True)


DATE_CHOICES = [(x, str(x)) for x in range(1, 13)]
YEAR_CHOICES = [(x, str(x)) for x in range(datetime.now().year, datetime.now().year + 13)]


class Payment(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    card_number = models.CharField(max_length=16, validators=[RegexValidator('^[0-9]*$'), MinLengthValidator(16)])
    card_year = models.IntegerField(choices=YEAR_CHOICES, default=1)
    card_month = models.IntegerField(choices=DATE_CHOICES, default=1)
    card_CVC = models.CharField(max_length=3, validators=[RegexValidator('^[0-9]*$'), MinLengthValidator(3)])


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart = models.ManyToManyField(Cart)
    payment_info = models.ForeignKey(Payment, on_delete=models.CASCADE)
    contact_info = models.ForeignKey(ContactInformation, on_delete=models.CASCADE)
    processed = models.BooleanField()

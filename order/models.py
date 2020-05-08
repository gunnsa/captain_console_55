from django.db import models


# Create your models here.
class Order(models.Model):
    pass


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


class PickUp(models.Model):
    pass


class Payment(models.Model):
    pass


class ProcessedOrder(models.Model):
    pass

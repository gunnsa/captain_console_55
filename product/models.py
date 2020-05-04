from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_lengt=255)
    manufacturer = models.CharField(max_length=255)
    short_description = models.CharField(max_length=255)
    long_description = models.CharField(max_length=999, blank=True)
    price = models.FloatField()
    on_sale = models.BooleanField()
    color = models.CharField(max_length=255)
    weight = models.FloatField()
    weight_unit = models.CharField(max_length=255)

class ProductImage(models.Model):
    image = models.CharField(max_length=999)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
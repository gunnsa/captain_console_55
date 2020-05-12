from django.db import models


class Newsletter(models.Model):
    email = models.CharField(max_length=100)

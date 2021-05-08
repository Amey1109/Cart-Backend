from django.db import models
from django.contrib.auth.models import User


class Products(models.Model):
    product_name = models.CharField(max_length=20)

    def __str__(self):
        return self.product_name




class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Products)
    count = models.IntegerField(default=0)

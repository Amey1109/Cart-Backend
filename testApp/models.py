from django.db import models
from django.contrib.auth.models import User


class Products(models.Model):
    product_name = models.CharField(max_length=20)
    price = models.IntegerField(default=100)


    def __str__(self):
        return self.product_name


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,unique=True)
    products = models.ManyToManyField(Products)

from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from datetime import date
import datetime as DT


class Produc(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField(default=100)

    def __str__(self):
        return self.name

# * Intermediate


class Car(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    products = models.ManyToManyField(Produc, through='CartProduct')

    def __str__(self):
        return self.user_id.username


#! Main Cart
class CartProduct(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    product = models.ForeignKey(Produc, on_delete=models.CASCADE)
    cart = models.ForeignKey(Car, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username + self.product.name


class Order(models.Model):
    PAYMENT_METHODS = (
        ("ONLINE_PAY", "Online Payment"),
        ("COD_PAY", "Cash Payment"),
    )

    order_placed_by = models.ForeignKey(User, on_delete=models.CASCADE)
    total_products = models.IntegerField(default=0)
    order_total = models.IntegerField(default=100)
    payment_mode = models.CharField(
        null=False, choices=PAYMENT_METHODS, max_length=30, default='Cash Payment')
    products = models.TextField(default="")
    address = models.CharField(max_length=20, default="")
    order_completed = models.BooleanField(default=False)
    date_of_ordering = models.DateField(default=date.today)
    date_of_delivery = models.DateField(
        default=DT.date.today() + DT.timedelta(days=7))

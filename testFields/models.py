from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User


class Produc(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField(default=100)

    def __str__(self):
        return self.name


class Car(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    products = models.ManyToManyField(Produc, through='CartProduct')

    def __str__(self):
        return self.user_id.username


class CartProduct(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    product = models.ForeignKey(Produc, on_delete=models.CASCADE)
    cart = models.ForeignKey(Car, on_delete=models.CASCADE)

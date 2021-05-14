from django.db import models
from rest_framework import serializers
from .models import CartProduct

class CartProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = CartProduct
        fields = "__all__"
from rest_framework import serializers
from . models import Cart, Products


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ("url", "id", "product_name")


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ("url", "id", "user", "products", "count")

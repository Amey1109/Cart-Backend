from django.contrib import admin
from .models import Products, Cart


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name')


class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')


admin.site.register(Products, ProductAdmin)
admin.site.register(Cart, CartAdmin)

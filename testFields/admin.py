from django.contrib import admin
from testFields.models import Produc, CartProduct, Car, Order




class CartProductAdmin(admin.ModelAdmin):
    list_display=("id","user","product","cart")


admin.site.register(Car)
admin.site.register(CartProduct,CartProductAdmin)
admin.site.register(Produc)
admin.site.register(Order)




from django.urls import path, include
from testFields.views import add_to_cart, get_cart_details, remove_from_cart

urlpatterns = [
    path('get_cart/', get_cart_details),
    path('add_cart/', add_to_cart),
    path('delete_cart/', remove_from_cart),





]

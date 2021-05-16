
from django.urls import path, include
from testFields.views import add_to_cart, complete_order, get_cart_details, get_order_details, place_order, remove_from_cart

urlpatterns = [
    path('get_cart/', get_cart_details),
    path('add_cart/', add_to_cart),
    path('delete_cart/', remove_from_cart),
    path('place_order/', place_order),
    path('complete_order/', complete_order),
    path('get_order_details/', get_order_details)


]

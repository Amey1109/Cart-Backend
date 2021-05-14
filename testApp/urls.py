from django.urls import path, include
from .views import getCart, addToCart, removeFromCart
urlpatterns = [

    path('getCart/<int:id>', getCart),
    path('addToCart/', addToCart),
    path('removeFromCart/<int:id>', removeFromCart),

]


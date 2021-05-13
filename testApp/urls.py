from django.urls import path, include
from .views import getCart, addToCart, removeFromCart
urlpatterns = [

    path('getCart/<int:id>', getCart),
    path('addToCart/', addToCart),
    path('removeFromCart/<int:id>', removeFromCart),

]


# animals = ['cat','dog','dog','camel','camel','giraffe','king kong']
# animal_count = {}
# for animal in animals:
#  if animal in animal_count:
#  animal_count.update({animal : animal_count[animal] + 1})
#  else:
#  animal_count.update({animal : 1}) 
# print(animal_count)
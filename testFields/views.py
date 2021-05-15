from django.db.models import query
from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import serializers

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import CartProduct, Car, Produc
from django.contrib.auth.models import User
from .serializers import CartProductSerializers
from django.views.decorators.csrf import csrf_exempt


@api_view(['GET'])
def get_cart_details(request):
    query_set = CartProduct.objects.filter(user=request.data['id'])
    product_data = []
    result = []
    price = 0
    for item in query_set:
        price = price + item.product.price
        product_data.append({
            'product_name': item.product.name,
            'product_price': item.product.price,
        })

    result.append(
        {
            'cart_owner_id': item.user.id,
            'cart_owner_name': item.cart.user_id.username,
            'product': product_data,
            'cart_price': price
        }
    )

    return JsonResponse(result, safe=False)


@api_view(['POST'])
def add_to_cart(request):
    try:
        cart_user = Car.objects.get(user_id=request.data['id'])
        user_instance = User.objects.get(id=request.data['id'])
        product_instance = Produc.objects.get(id=request.data['product_id'])
        cart = CartProduct(user=user_instance,
                           product=product_instance, cart=cart_user)
        cart.save()
        return Response({"msg": "Item added to the Cart"})

    except Car.DoesNotExist as e:
        user_instance = User.objects.get(id=request.data['id'])
        new_cart_user = Car(user_id=user_instance)
        new_cart_user.save()
        user_instance = User.objects.get(id=request.data['id'])
        product_instance = Produc.objects.get(id=request.data['product_id'])
        cart = CartProduct(user=user_instance,
                           product=product_instance, cart=new_cart_user)
        cart.save()
        return Response({"msg": "Item added to the Cart "})


@csrf_exempt
@api_view(['POST'])
def remove_from_cart(request):
    user_instance = User.objects.get(id=request.data['id'])
    cart_user = Car.objects.get(user_id=user_instance)
    product_instance = Produc.objects.get(id=request.data['product_id'])

    cart = CartProduct.objects.filter(
        user=user_instance, product=product_instance, cart=cart_user)
    cart.delete()
    return Response({"msg": "Item Deleted"})

@api_view(['POST'])
def place_order(request):
    query_set = CartProduct.objects.filter(user=request.data['id'])
    result = []
    order_total = 0 
    
    for item in query_set:
        order_total = order_total +item.product.price
        



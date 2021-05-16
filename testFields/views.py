from django.db.models import query
from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import serializers

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import CartProduct, Car, Order, Produc
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
    total_products = 0
    products = ""
    for item in query_set:
        order_total = order_total + item.product.price
        total_products = total_products + 1
        products = item.product.name + ":" + \
            str(item.product.price) + ", " + products

    user_instance = User.objects.get(id=request.data['id'])
    order = Order(order_placed_by=user_instance,
                  total_products=total_products,
                  order_total=order_total,
                  payment_mode=request.data["payment_mode"],
                  products=products, address="ADD1")

    order.save()
    result.append({
        "order_id": order.id,
        "order_placed_by": item.user.id,
        "total_products": total_products,
        "order_total": order_total,
        "date_of_ordering": order.date_of_ordering,
            "date_of_delivery": order.date_of_delivery,

        "order_completed": False
    })

    query_set.delete()

    return JsonResponse(result, safe=False)


@api_view(['PUT'])
def complete_order(request):
    order_object = Order.objects.get(id=request.data['id'])
    order_object.order_completed = True
    order_object.save()

    return Response({"status": True, "message": "Order Dispatched"})


@api_view(['POST'])
def get_order_details(request):
    user_instance = User.objects.get(id=request.data['id'])
    order_object = Order.objects.filter(order_placed_by=user_instance)
    result = []

    for order in order_object:
        result.append({
            "order_id": order.id,
            "ordered_products": order.products,
            "total_products": order.total_products,
            "order_total": order.order_total,
            "date_of_ordering": order.date_of_ordering,
            "date_of_delivery": order.date_of_delivery,

            "order_completed": order.order_completed
        })

    return JsonResponse(result, safe=False)

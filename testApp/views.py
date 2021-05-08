from django.shortcuts import render
from django.http import JsonResponse
from .models import Products, Cart

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.test import APIRequestFactory


from .serializers import CartSerializer

factory = APIRequestFactory()
request = factory.get('/')
serializer_context = {
    'request': Request(request),
}


@api_view(['GET'])
def getCart(request, id):
    query_set = Cart.objects.filter(user=id)
    result = []
    for objects in query_set:
        product_list = []
        products = objects.products.all() #[1,2,3]
        for product in products:
            product_list.append(product.product_name)

        data = {
            'id': objects.id,
            'user': objects.user.pk,
            'products': product_list
        }

        result.append(data)

    # serializer_object = CartSerializer(
    #     query_set, many=True, context=serializer_context)
    # if serializer_object:
    #     return JsonResponse(serializer_object.data, safe=False)
    # else:
    return JsonResponse(result, safe=False)


@api_view(['POST'])
def addToCart(request, id):
    products = [1, 2, 3, 4]
    product_list = list(request.data['products'])
    try:
        cart_object = Cart.objects.get(user=id)
        cart_object.products.add(*products)
        cart_object.save()

        return Response({"msg": "Added to Cart"})
    except Cart.DoesNotExist as e:
        return Response({"msg": "Cart does not exist"})


@api_view(['POST'])
def removeFromCart(request, id):
    products = [4]
    try:
        cart_object = Cart.objects.get(user=id)
        cart_object.products.remove(*products)
        cart_object.save()

        return Response({"msg": "removed from Cart"})
    except Cart.DoesNotExist as e:
        return Response({"msg": "Cart does not exist"})

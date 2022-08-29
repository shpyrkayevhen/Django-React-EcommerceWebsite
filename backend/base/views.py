from django.shortcuts import get_object_or_404, get_list_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import ProductSerialezer
from .models import Product


@api_view(['GET'])
def getRoutes(request):

    routes = [
        '/api/products',
        '/api/products/create/',

        '/api/products/upload/',

        '/api/products/<id>/reviews/',

        '/api/products/top/',
        '/api/products/<id>/',

        '/api/products/delete/<id>/',
        '/api/products/update/<id>/',
    ]

    return Response(routes)


@api_view(['GET'])
def getProducts(request):

    products = get_list_or_404(Product)
    serializer = ProductSerialezer(products, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def getProduct(request, pk):

    product = get_object_or_404(Product, _id=pk)
    serializer = ProductSerialezer(product)

    return Response(serializer.data)

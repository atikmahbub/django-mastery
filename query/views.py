from django.shortcuts import render

# Create your views here.
from .models import Product, RejectedProduct
from .serializers import ProductSerializer, RejectedProductSerializer
from rest_framework import generics


class ProductView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class RejectedProductView(generics.ListCreateAPIView):
    queryset = RejectedProduct.objects.all()
    serializer_class = RejectedProductSerializer

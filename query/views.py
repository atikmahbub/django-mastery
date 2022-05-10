from django.shortcuts import render

# Create your views here.
from .models import Product
from .serializers import ProductSerializer
from rest_framework import generics


class ProductView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

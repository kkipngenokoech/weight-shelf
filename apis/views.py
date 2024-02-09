from django.shortcuts import render
from rest_framework import viewsets
from .models import Product, Shelf
from .serializers import ProductSerializer, ShelfSerializer

# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ShelfViewSet(viewsets.ModelViewSet):
    queryset = Shelf.objects.all()
    serializer_class = ShelfSerializer

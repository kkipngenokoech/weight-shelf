from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Product, Shelf
from .serializers import ProductSerializer, ShelfSerializer

# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ShelfViewSet(viewsets.ModelViewSet):
    queryset = Shelf.objects.all()
    serializer_class = ShelfSerializer

    @action(detail=True, methods=['get'])
    def check_weight(self, request, pk=None):
        shelf = self.get_object()
        return Response({'weight': shelf.check_weight()})

# converts django model instances to json data for api responses
from .models import Product, Shelf
from rest_framework import serializers

class ShelfSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shelf
        fields = ['id', 'name', 'description', 'weight_capacity', 'total_current_weight']


class ProductSerializer(serializers.ModelSerializer):
    shelf_id = serializers.PrimaryKeyRelatedField(queryset=Shelf.objects.all(), source='shelf', write_only=True)
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'stock', 'weight', 'image_url', 'description', 'shelf', 'shelf_id']

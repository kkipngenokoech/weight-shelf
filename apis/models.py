from django.db import models

# Create your models here.
class Product (models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    weight = models.FloatField()
    image_url = models.CharField(max_length=2083)
    description = models.CharField(max_length=2083)
    shelf = models.ForeignKey('Shelf', related_name='products', on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return self.name
    
class Shelf (models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=2083)
    weight_capacity = models.FloatField()

    def total_current_weight(self):
        return sum(product.weight for product in self.products.all())

    def __str__(self):
        return self.name
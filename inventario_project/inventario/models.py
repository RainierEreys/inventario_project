from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    marca = models.CharField(max_length=50)
    cantidad_min = models.IntegerField()
    cantidad_max = models.IntegerField()
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    

class Order(models.Model):
    date_time = models.DateTimeField()
    


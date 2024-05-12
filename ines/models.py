from django.db import models

# Create your models here.
class Ine(models.Model):
    nombre = models.CharField(max_length=255)
    calle = models.CharField(max_length=255)
    colonia = models.CharField(max_length=255)
    codigo_postal = models.CharField(max_length=10)
    ciudad = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    fecha_nacimiento = models.CharField(max_length=100)
    sexo = models.CharField(max_length=1)
    url = models.URLField()
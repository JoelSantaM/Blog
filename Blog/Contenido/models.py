from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return str(self.nombre)

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    cuerpo =models.TextField()

    def __str__(self):
        return str(self.nombre)
    
from django.db import models

# Create your models here.

class Producto(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    fecha_publicacion = models.DateField()
    categoria = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)

    def __str__(self):
        return str(self.titulo)
    
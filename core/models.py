from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Articulo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    ubicacion = models.CharField(max_length=100)
    fecha_subida = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    imagen = models.ImageField(upload_to='articulos/', null=False, blank=False)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=False,blank=False)

    def __str__(self):
        return self.nombre


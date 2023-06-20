from django.db import models

# Create your models here.
class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name="Id de Categoria")
    nombreCategoria = models.CharField(max_length=50, blank=True, verbose_name="Nombre de Categoria")

    def __str__(self):
        return self.nombreCategoria #permite acceder a los objetos a través de su nombre en el admin
    
class Stock(models.Model):
    code = models.CharField(primary_key=True, max_length=5, verbose_name="Codigo")
    nombre = models.CharField(max_length=50, blank=True, verbose_name="Nombre")
    precio = models.CharField(max_length=50, blank=True, verbose_name="Precio")
    imagen=models.ImageField(upload_to="imagenes", null=True, blank=True, verbose_name="Imagen")
    cantidad = models.IntegerField(max_length=5, blank=True, verbose_name="Cantidad")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name="Categoria")

    def __str__(self):
        return self.code
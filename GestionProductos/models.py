from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre=models.CharField(max_length=30)
    descripcion=models.CharField(max_length=255)

    def __str__ (self):
        return self.nombre

class Producto(models.Model):
    nombre=models.CharField(max_length=30)
    precio=models.IntegerField()
    ruta_imagen=models.CharField(max_length=255)
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)

    def __str__ (self):
        return self.nombre
    
class Comentario(models.Model):
    nombre=models.CharField(max_length=50)
    correo=models.EmailField()
    comentario=models.CharField(max_length=250)

    def __str__ (self):
        return self.nombre+ " : "+ self.comentario

class Pedido(models.Model):
    fecha = models.DateField()
    total = models.FloatField()
    estado= models.BooleanField(default=0)
    productos = models.ManyToManyField(Producto)

    def __str__ (self):
        return "El numero de pedido es: %d "% self.id

    

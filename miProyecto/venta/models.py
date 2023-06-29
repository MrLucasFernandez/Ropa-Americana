from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Categoria(models.Model):
    id_categoria    = models.BigAutoField(db_column='idCategoria', primary_key=True)
    descripcion     = models.CharField(max_length=25)
    
    def __str__(self):
        return str(self.descripcion)

class Producto(models.Model):
    id_producto     = models.BigAutoField(db_column='idProducto', primary_key=True)
    id_categoria    = models.ForeignKey('Categoria', on_delete=models.CASCADE, db_column='idCategoria')
    nombre          = models.CharField(max_length=25)
    marca           = models.CharField(max_length=25)
    descripcion     = models.CharField(max_length=200)
    talla           = models.CharField(max_length=4)
    precio          = models.IntegerField()
    stock           = models.IntegerField()
    imagen          = models.ImageField(upload_to='productos/', null=True)

    def __str__(self):
        return "ID: "+str(self.id_producto)+" "+str(self.nombre)+" /"+str(self.id_categoria)

class Cliente(models.Model):#Tomar como referencia tabla usuarios
    username        = models.CharField(max_length=20, primary_key=True)
    rut             = models.CharField(max_length=9)
    pnombre         = models.CharField(max_length=15)
    snombre         = models.CharField(max_length=15, blank=True, null=True)
    appaterno       = models.CharField(max_length=15)
    apmaterno       = models.CharField(max_length=15, blank=True, null=True)
    email           = models.EmailField(unique=True, max_length=60)
    contrasena      = models.CharField(max_length=20)
    direccion       = models.CharField(max_length=50)
    

    def __str__(self):
        return str(self.rut)+" "+str(self.pnombre)+" "+str(self.appaterno)
    
class Pedido(models.Model):#Quitar id_producto y cantidad
    id_pedido       = models.BigAutoField(db_column='id_pedido', primary_key=True)
    direccion       = models.ForeignKey('Cliente', on_delete=models.CASCADE, db_column='direccion',related_name='direccion_pedido')
    fecha           = models.DateField(blank=False, null=False)
    total           = models.IntegerField()
    email_cliente   = models.ForeignKey('Cliente', on_delete=models.CASCADE, db_column='email', related_name='email_cliente')

    def __str__(self):
        return str(self.id_pedido)+" "+str(self.fecha)


class Boleta(models.Model):#Referenciar bien la fecha
    id_boleta       = models.BigAutoField(db_column='id_boleta', primary_key=True)
    fecha           = models.ForeignKey('Pedido', on_delete=models.CASCADE, db_column='fecha', related_name='fecha_boleta')
    id_pedido       = models.ForeignKey('Pedido', on_delete=models.CASCADE, db_column='id_pedido', related_name='id_compra')
    total           = models.ForeignKey('Pedido', on_delete=models.CASCADE, db_column='total', related_name='total_boleta')
    
    def __str__(self):
        return str(self.id_boleta)+" "+str(self.fecha)
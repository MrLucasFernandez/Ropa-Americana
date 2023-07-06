from django.contrib import admin
from .models import Categoria,Producto,Pedido,Cliente, Boleta, Carrito

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Pedido)
admin.site.register(Cliente)
admin.site.register(Boleta)
admin.site.register(Carrito)
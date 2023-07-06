from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Categoria, Producto, Carrito, Pedido
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User

# Create your views here.
def prueba(request):
    prodMujer = Producto.objects.filter(id_categoria="1")
    context = {"productos":prodMujer}
    return render(request,"venta/prueba.html",context)


def index_view(request):
    request.session["usuario"]="lufernandezm"
    usuario = request.session["usuario"]
    productos = Producto.objects.all()
    context = {"usuario":usuario,"productos":productos}
    return render(request,'venta/index.html',context)

def carrito_view(request):
    productos = Carrito.objects.filter(usuario=request.user.username)
    imagenes = Producto.objects.all()
    suma = 0
    
    for i in productos:
        suma = suma + i.precio

    context = {"productos":productos,"imagenes":imagenes,"total":suma}
    
    return render(request, 'venta/carrito.html',context)

def detalle_view(request,pk):
    producto = Producto.objects.get(id_producto=pk)
    context = {"producto":producto}
    return render(request, 'venta/detalle.html',context)

def hombre_view(request):
    prodHombre = Producto.objects.filter(id_categoria="1")
    context = {"productos":prodHombre}
    return render(request,"venta/hombre.html",context)

def mujer_view(request):
    prodMujer = Producto.objects.filter(id_categoria="2")
    context = {"productos":prodMujer}
    return render(request,"venta/mujer.html",context)

def infantil_view(request):
    prodInfantil = Producto.objects.filter(id_categoria="3")
    context = {"productos":prodInfantil}
    return render(request,"venta/infantil.html",context)

def unisex_view(request):
    prodUnisex = Producto.objects.filter(id_categoria="4")
    context = {"productos":prodUnisex}
    return render(request,"venta/unisex.html",context)

def search(request):
    return render(request,"venta/search.html")

def producto_search(request):
    busqueda        = request.GET["prodbuscar"]
    productos       = Producto.objects.filter(nombre__icontains=busqueda)
    
    
    context     = {"productos":productos,"busqueda":busqueda}
    return render(request,"venta/search.html",context)

def login_view(request):
    return render(request, 'venta/login.html')

def usuarioAdd(request):
    
    username      = request.POST["username"]
    email         = request.POST["email"]
    first_name    = request.POST["first_name"]
    last_name     = request.POST["last_name"]
    password      = request.POST["password"]
    
    
    objUser=User.objects.create_user(username   = username,
                                    email       = email,
                                    first_name  = first_name,
                                    last_name   = last_name,
                                    password    = password)
    
    objUser.save()
    
    return render(request,'venta/index.html')

def register_view(request):
    return render(request, 'venta/register.html')

@staff_member_required
def producto_add(request):
    
    if request.method != "POST":
        lista_categorias = Categoria.objects.all()
        context = {"categorias":lista_categorias}
        return render(request,'venta/producto_add.html', context)
    else:
        
        categoria   = request.POST["categoria"]
        nombre      = request.POST["nombre"]
        marca       = request.POST["marca"]
        descripcion = request.POST["descripcion"]
        talla       = request.POST["talla"]
        precio      = request.POST["precio"]
        stock       = request.POST["stock"]
        imagen      = request.FILES["imagen"]

        objCategoria= Categoria.objects.get(id_categoria = categoria)
        
        objProducto = Producto.objects.create(
            id_categoria     = objCategoria,
            nombre           = nombre,
            marca            = marca,
            descripcion      = descripcion,
            talla            = talla,
            precio           = precio,
            stock            = stock,
            imagen           = imagen)
        
        objProducto.save()
        
        lista_categorias = Categoria.objects.all()
        lista_productos = Producto.objects.all()
        context = {"mensaje":"Producto registrado correctamente","productos":lista_productos}
        return render(request,'venta/producto_mod.html', context)

@staff_member_required
def producto_mod(request):
    lista_productos = Producto.objects.all()
    context = {"productos":lista_productos}
    return render(request,'venta/producto_mod.html', context)

"""
@staff_member_required
def producto_store(request,pk):
    prod = Producto.objects.get(id_producto=pk)
    context = {"prod":prod}
    print(prod.id_producto)
    return render(request,'venta/producto_mod.html', context)"""

@staff_member_required
def producto_del(request,pk):
    try:
        prod = Producto.objects.get(id_producto=pk)
        prod.delete()
        mensaje = "El producto se ha eliminado"
        lista_productos = Producto.objects.all()
        context = {"productos":lista_productos, "mensaje":mensaje}
        return render(request,'venta/producto_mod.html', context)
    except:
        mensaje = "El producto NO ha sido eliminado"
        lista_productos = Producto.objects.all()
        context = {"productos":lista_productos, "mensaje":mensaje}
        return render(request,'venta/producto_mod.html', context)

@staff_member_required
def producto_find(request,pk):
    if pk != "":
        producto = Producto.objects.get(id_producto=pk)
        lista_categorias = Categoria.objects.all() 
        
        context = {"producto":producto, "categorias":lista_categorias}
        return render(request,'venta/producto_edit.html', context)
    else:
        mensaje = "El producto NO existe"
        context = {"mensaje":mensaje}
        return render(request,'venta/producto_mod.html', context)

@staff_member_required
def producto_update(request):
    
    if request.method == "POST":
        
        idprod      = request.POST["idprod"]
        categoria   = request.POST["categoria"]
        nombre      = request.POST["nombre"]
        marca       = request.POST["marca"]
        descripcion = request.POST["descripcion"]
        talla       = request.POST["talla"]
        precio      = request.POST["precio"]
        stock       = request.POST["stock"]
        imagen      = request.FILES["imagen"]
        """
        if request.FILES["imagen"] != None:
            imagen = request.FILES["imagen"]
        else:
            prod=Producto.objects.get(id_producto=idprod)
            imagen = prod.imagen"""
        #arreglar imagen

        objCategoria = Categoria.objects.get(id_categoria = categoria)
        objProducto = Producto()
        
        
        objProducto.id_producto     = idprod
        objProducto.id_categoria    = objCategoria
        objProducto.nombre          = nombre
        objProducto.marca           = marca
        objProducto.descripcion     = descripcion
        objProducto.talla           = talla
        objProducto.precio          = precio
        objProducto.stock           = stock
        objProducto.imagen          = imagen
        
        
        objProducto.save()
        lista_categorias = Categoria.objects.all()
        lista_productos = Producto.objects.all()
        context = {"mensaje":"El producto se ha actualizado correctamente", "categorias":lista_categorias, "producto":objProducto,"productos":lista_productos}
        return render(request,'venta/producto_mod.html', context)
    else:
        lista_productos = Producto.objects.all()
        context = {"productos":lista_productos}
        return render(request,'venta/producto_mod.html', context)

@login_required
def usuario(request):
    request.session["usuario"]="lucasfernandezm"
    usuario = request.session["usuario"] 
    context = {"usuario":usuario}
    return render(request,'venta/usuario.html',context)

@login_required
def carrito_add(request,pk):
    
    if request.user.is_authenticated:
        
        producto    = Producto.objects.get(id_producto=pk)

        id_producto = producto.id_producto
        categoria   = producto.id_categoria
        nombre      = producto.nombre
        marca       = producto.marca
        descripcion = producto.descripcion
        talla       = producto.talla
        precio      = producto.precio
        usuario     = request.user.username
        print(nombre)

        
        
        objCarrito = Carrito.objects.create(
            id_producto      = id_producto,
            id_categoria     = categoria,
            nombre           = nombre,
            marca            = marca,
            descripcion      = descripcion,
            talla            = talla,
            precio           = precio,
            usuario          = usuario)
        
        objCarrito.save()
        
        
        
        context = {"producto":producto,"mensaje":"¡Producto agregado!"}
        return render(request,'venta/detalle.html',context)

    else:
        print("User is not logged in :(")
        return render(request,'venta/detalle.html', context)
        
@login_required
def carrito_del(request):
    try:
        carro = Carrito.objects.filter(usuario=request.user.username)
        
        for i in carro:
            
            producto = Producto.objects.get(id_producto=i.id_producto)
            producto.stock = producto.stock - 1
            
            if producto.stock <1:
                producto.stock = 0
                producto.save()
            else:
                producto.save()
            
        
        carro.delete()
        return render(request,'venta/index.html')
    except:
        mensaje = "El producto NO ha sido eliminado"
        lista_productos = Producto.objects.all()
        context = {"productos":lista_productos, "mensaje":mensaje}
        return render(request,'venta/index.html', context)
    
def pedido_view(request):
    return render(request, 'venta/pedido.html')
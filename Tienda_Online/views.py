from django.http import HttpResponse
from django.template import Template,Context
from django.shortcuts import render, get_object_or_404,redirect
from GestionProductos.models import Producto,Categoria
from Tienda_Online.forms import FormularioContacto
from GestionProductos.models import Comentario, Pedido
from django.db.models import Q
import datetime

def bienvenida(request):
    return HttpResponse("Bienvenidos")

def comentario(request):
    documento = '<h1 style="color: #ABE43A;" > Dejanos tu comentario </h1>'
    return HttpResponse(documento)

def calcular_precio(request,numero):
    total = numero *5
    return HttpResponse("El total a pagar es: %s " %total)

def plantilla(request):
    ctx= {"curso":"Desarrollo Web","anio":2026}

    return render(request,'plantilla.html',ctx)

def plantilla2(request):
    doc_externo = open(r"C:\Users\MAYKER\Desktop\Pagina_Web\venv\Tienda_Online\Tienda_Online\templates\plantilla2.html")
    template = Template(doc_externo.read())
    doc_externo.close()

    ctx= Context()

    documento = template.render(ctx)

    return HttpResponse(documento)

def inicio(request):
    return render(request,'inicio.html')

def productos(request):
    
    #lista_productos = Producto.objects.raw('Select * from "GestionProductos_producto" where precio < 5000')
    #lista_productos = Producto.objects.all()

    #lista_productos = Producto.objects.filter(precio__lt=5000) #__lt es igual a menor que
    
    #Condiciones que sea deteminada categoria y determinado precio
    lista_productos = Producto.objects.filter(categoria__nombre='Computadoras', precio__lt=8000)
    return render(request,'productos.html',{'productos':lista_productos})

def categoria(request):
    lista_categorias = Categoria.objects.all()

    if(request.GET.get('categoria')):
        categoria_a_buscar = get_object_or_404(Categoria,id = request.GET["categoria"])
        lista_productos = Producto.objects.filter(categoria=categoria_a_buscar)
    else:
        lista_productos= Producto.objects.all()

    return render(request,'categoria.html',
                  {
                    'productos':lista_productos,
                    'lista_categorias':lista_categorias
                  },
                  )

def contactanos(request):

    if request.method=="POST":
        formulario = FormularioContacto(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            return render(request,"inicio.html")
    else:
        formulario = FormularioContacto()
    
    return render(request,'contactanos.html',{'form':formulario})




def carrito(request):
   

    productos_agregados= Pedido.objects.prefetch_related('productos')
    return render(request,'carrito.html',{'pedidos':productos_agregados})


def agregar_al_carrito(request,id_producto):

    pedido = Pedido.objects.get_or_create(
        fecha=datetime.datetime.now()
    )
    producto_agregar = Producto.objects.get(id=id_producto)

    pedido.total = pedido.total + producto_agregar.precio
    pedido.productos.add(producto_agregar)

    return render(request,'carrito.html')














def Guardar_Producto(request):

    pr= Producto.objects.create(
        nombre = "Mouse",
        precio = 200,
        ruta_imagen = "https://upload.wikimedia.org/wikipedia/commons/2/22/3-Tasten-Maus_Microsoft.jpg"
    )

    return HttpResponse("Se ha guardado con exito el producto")


def GuardarInformacion(request):

    if request.method=="POST":
        formulario = FormularioContacto(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            
            c_guardar= Comentario.objects.create(
                nombre=info["nombre"],
                correo=info["correo"],
                comentario=info["comentario"]

            )
            return redirect('productos')
    else:
        return HttpResponse("Ha ocurrido un error")
    
def agregar_al_carrito(request, id_producto):

    producto_a_agregar= get_object_or_404(Producto, id= id_producto)

    pedido_pendiente = pedido= Pedido.objects.filter(estado=0,fecha=datetime.datetime.now()).first()

    if(pedido_pendiente):
        pedido_pendiente.productos.add(producto_a_agregar)
        pedido_pendiente.total=pedido_pendiente.total + producto_a_agregar.precio
        pedido_pendiente.save()
    else:    
        pedido= Pedido.objects.create(
            fecha=datetime.datetime.now(),
            total = producto_a_agregar.precio,
        )

        pedido.productos.add(producto_a_agregar)
   
    return redirect ('carrito')






def consultas(request):

    #Crear un nuevo registro
    registro = Producto.objects.create(nombre="Producto 1")

    #Actualizar un registro
    registro_prueba = Producto.objects.get(id=1)
    registro_prueba.nombre = "Nuevo Nombre"
    registro_prueba.save()

    #Eliminar un registro
    registro_eliminar = Producto.objects.get(id=1)
    registro_eliminar.delete()

    #Consultar todos los registros
    registros = Producto.objects.all()

    #Consultar por campos especificos
    consulta = Producto.objects.only('nombre')

    #Consultar por una condicion
    consulta_especifica = Producto.objects.filter(nombre__contains = 's') #funciona como like en sql __contains

    #Consultar por varias condiciones
    #get funciona para buscar solo un registro
    #filter funciona para buscar varios o un listado de registros
    registro1=Producto.objects.get(nombre='Laptops',id=1)
    registros = Producto.objects.filter(nombre__contains = 's', id = 2)

    #Consulta OR
    consulta_or =Producto.objects.get(Q(nombre='Laptops')|Q(id=2))

    #Consulta NOT o excluyente
    consulta_not = Producto.objects.exclude(id=1)

    #Consultas JOIN
    productos = Producto.objects.select_related('categoria')

    #Consulta ordenada
    listado_productos = Producto.objects.all().order_by('id') #Ascendente
    listado_productos = Producto.objects.all().order_by('-id') #Descendente

    #Ordenar por llave foránea
    consulta_ordenada = Producto.objects.all().order_by('categoria__nombre')

    #Consulta SQL directa
    consulta_sql = Producto.objects.raw('Select * from "GestionProductos_producto" ')

    #Condiciones de Comparacion
    #__gt es: mayor que
    #__lt es: menor que
    #__gte es: mayor o igual que
    #__ lte es: menor o igual que

    return HttpResponse("Se ha realizado correctamente")



"""
URL configuration for Tienda_Online project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Tienda_Online.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bienvenida/',bienvenida, name='bienvenida'),
    path('comentario/',comentario, name='comentario'),
    path('calcular_precio/<int:numero>/',calcular_precio, name='calcularprecio'),
    path('plantilla/',plantilla, name='plantilla'),
    path('plantilla2/',plantilla2, name='plantilla2'),
    path('inicio/',inicio, name='inicio'),
    path('productos/',productos, name='productos'),
    path('categoria/',categoria, name='categoria'),
    path('carrito/',carrito, name='carrito'),
    path('contactanos/',contactanos, name='contactanos'),
    path('Guardar_Producto/',Guardar_Producto),
    path('GuardarInformacion/',GuardarInformacion),
    path('agregar_al_carrito/int:<id_producto>',agregar_al_carrito, name='agregar_al_carrito' ),
]

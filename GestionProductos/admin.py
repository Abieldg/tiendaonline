from django.contrib import admin
from .models import Categoria,Producto,Comentario,Pedido

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(Comentario)
admin.site.register(Pedido)
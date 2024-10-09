from django.shortcuts import render, HttpResponse
from app.models import Producto

def vista_home(request):
    return render(request, 'body.html')


def lista_producto(request):
    
    nombre = {
    'titulo' : 'Listado de productos:',
    'productos': Producto.objects.all()
    }
    return render(request, 'categorias/producto/producto.html', nombre)
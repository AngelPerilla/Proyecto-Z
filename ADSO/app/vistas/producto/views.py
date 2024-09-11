from typing import Any
from django.views.generic import ListView
from django.shortcuts import render
from app.models import Producto

def lista_producto(request):
    
    listado = {
    'titulo' : 'Listado de productos:',
    'productos': Producto.objects.all()
    }
    return render(request, 'categorias/producto.html', listado)

class ProductoListView(ListView):
    model = Producto
    template_name = 'categorias/producto.html'
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de productos'
        return context
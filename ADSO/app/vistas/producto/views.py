from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.http import JsonResponse
from django.views.generic import ListView, CreateView
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect

from app.models import Producto
from app.forms import ProductoForm

def lista_producto(request):
    
    listado = {
    'titulo' : 'Listado de productos:',
    'productos': Producto.objects.all()
    }
    return render(request, 'categorias/producto.html', listado)

class ProductoListView(ListView):
    model = Producto
    template_name = 'categorias/producto.html'
    
    @method_decorator(csrf_exempt)
    def dispatch (self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        alerta = {'alerta' : 'Pillado'}
        return JsonResponse(alerta)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de productos'
        return context

class ProductoCreateView(CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'crear.html'
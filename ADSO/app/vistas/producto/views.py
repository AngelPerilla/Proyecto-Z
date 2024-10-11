from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from app.models import Producto
from app.forms import ProductoForm


def lista_producto(request):
    
    listado = {
    'titulo' : 'Listado de productos:',
    'productos': Producto.objects.all()
    }
    return render(request, 'categorias/producto/producto.html', listado)

@method_decorator(login_required, name='dispatch')
@method_decorator(never_cache, name='dispatch')
class ProductoListView(ListView):
    model = Producto
    template_name = 'categorias/producto/producto.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de productos'
        context['crear_url'] = reverse_lazy('app:producto_crear')
        context['entidad'] = 'Productos'
        return context

@method_decorator(login_required, name='dispatch')
@method_decorator(never_cache, name='dispatch')
class ProductoCreateView(CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'categorias/producto/crear.html'
    success_url = reverse_lazy('app:producto_lista')

    @method_decorator(csrf_exempt)
    def dispatch (self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(self.success_url)
        else:
            return self.render_to_response(self.get_context_data(form=form))
    
def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs) 
    context['titulo'] = 'Crear Producto'
    context['listar_url'] = reverse_lazy('app:producto_lista')
    context['entidad'] = 'Productos'

    return context
    
def form_valid(self, form):
    form.save()
    return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
@method_decorator(never_cache, name='dispatch')
class ProductoUpdateView(UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'categorias/producto/crear.html'
    success_url = reverse_lazy('app:producto_lista')
    
    @method_decorator(csrf_exempt)
    def dispatch (self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, instance=self.get_object())
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(self.success_url)
        else:
            return self.render_to_response(self.get_context_data(form=form))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        context['titulo'] = 'Editar Producto'
        context['listar_url'] = reverse_lazy('app:producto_lista')
        context['entidad'] = 'Productos'
        return context
    
@method_decorator(login_required, name='dispatch')
@method_decorator(never_cache, name='dispatch')
class ProductoDeleteView(DeleteView):
    model = Producto
    template_name = 'categorias/producto/eliminar.html'
    success_url = reverse_lazy('app:producto_lista')
    
    @method_decorator(csrf_exempt)
    def dispatch (self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        producto = self.get_object()
        producto.delete()
        return HttpResponseRedirect(self.success_url)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        context['titulo'] = 'Eliminar Producto'
        context['listar_url'] = reverse_lazy('app:producto_lista')
        context['entidad'] = 'Productos'
        return context



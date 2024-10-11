from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from app.models import Cliente
from app.forms import ClienteForm


def lista_cliente(request):
    
    listado = {
    'titulo' : 'Listado de clientes:',
    'clientes': Cliente.objects.all()
    }
    return render(request, 'categorias/cliente/cliente.html', listado)
@method_decorator(login_required, name='dispatch')
@method_decorator(never_cache, name='dispatch')
class ClienteListView(ListView):
    model = Cliente
    template_name = 'categorias/cliente/cliente.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de clientes'
        context['crear_url'] = reverse_lazy('app:cliente_crear')
        context['entidad'] = 'Clientes'
        return context

@method_decorator(login_required, name='dispatch')
@method_decorator(never_cache, name='dispatch')
class ClienteCreateView(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'categorias/cliente/crear.html'
    success_url = reverse_lazy('app:cliente_lista')
    
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
        context['titulo'] = 'Ingresar Cliente'
        context['listar_url'] = reverse_lazy('app:cliente_lista')
        context['entidad'] = 'Clientes'
        return context
    
@method_decorator(login_required, name='dispatch')
@method_decorator(never_cache, name='dispatch')
class ClienteUpdateView(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'categorias/cliente/crear.html'
    success_url = reverse_lazy('app:cliente_lista')
    
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
        context['titulo'] = 'Editar Información del cliente'
        context['listar_url'] = reverse_lazy('app:cliente_lista')
        context['entidad'] = 'Clientes'
        return context
    
@method_decorator(login_required, name='dispatch')
@method_decorator(never_cache, name='dispatch')
class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = 'categorias/cliente/eliminar.html'
    success_url = reverse_lazy('app:cliente_lista')
    
    @method_decorator(csrf_exempt)
    def dispatch (self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        cliente = self.get_object()
        cliente.delete()
        return HttpResponseRedirect(self.success_url)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        context['titulo'] = 'Eliminar Cliente'
        context['listar_url'] = reverse_lazy('app:cliente_lista')
        context['entidad'] = 'Clientes'
        return context
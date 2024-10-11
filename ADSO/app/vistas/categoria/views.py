from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from app.models import Categoria
from app.forms import CategoriaForm

def lista_categoria(request):
    
    listado = {
    'titulo' : 'Listado de categorías:',
    'categorias': Categoria.objects.all()
    }
    return render(request, 'categorias/categoria/categoria.html', listado)

@method_decorator(login_required, name='dispatch')
@method_decorator(never_cache, name='dispatch')
class CategoriaListView(ListView):
    model = Categoria
    template_name = 'categorias/categoria/categoria.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de categorías'
        context['crear_url'] = reverse_lazy('app:categoria_crear')
        context['entidad'] = 'Categoria'
        return context

@method_decorator(login_required, name='dispatch')
@method_decorator(never_cache, name='dispatch')
class CategoriaCreateView(CreateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'categorias/categoria/crear.html'
    success_url = reverse_lazy('app:categoria_lista')
    
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
        context['titulo'] = 'Ingresar categoría'
        context['listar_url'] = reverse_lazy('app:categoria_lista')
        context['entidad'] = 'Categorias'
        return context
    
@method_decorator(login_required, name='dispatch')
@method_decorator(never_cache, name='dispatch')
class CategoriaUpdateView(UpdateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'categorias/categoria/crear.html'
    success_url = reverse_lazy('app:categoria_lista')
    
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
        context['titulo'] = 'Editar Información del categoria'
        context['listar_url'] = reverse_lazy('app:categoria_lista')
        context['entidad'] = 'Categorias'
        return context
    
@method_decorator(login_required, name='dispatch')
@method_decorator(never_cache, name='dispatch')
class CategoriaDeleteView(DeleteView):
    model = Categoria
    template_name = 'categorias/categoria/eliminar.html'
    success_url = reverse_lazy('app:categoria_lista')
    
    @method_decorator(csrf_exempt)
    def dispatch (self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        categoria = self.get_object()
        categoria.delete()
        return HttpResponseRedirect(self.success_url)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        context['titulo'] = 'Eliminar categoria'
        context['listar_url'] = reverse_lazy('app:categoria_lista')
        context['entidad'] = 'Categorias'
        return context
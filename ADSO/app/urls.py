from django.urls import path
from app.vistas.producto.views import *
from app.vistas.cliente.views import *

app_name = 'app'
urlpatterns = [
    # urls Producto
    path('producto/listar/', ProductoListView.as_view(), name= 'producto_lista'),
    path('producto/crear/', ProductoCreateView.as_view(), name = 'producto_crear'),
    path('producto/editar/<int:pk>/', ProductoUpdateView.as_view(), name = 'producto_editar'),
    path('producto/eliminar/<int:pk>/', ProductoDeleteView.as_view(), name = 'producto_eliminar'),

    # urls Cliente
    path('cliente/listar/', ClienteListView.as_view(), name= 'cliente_lista'),
    path('cliente/crear/', ClienteCreateView.as_view(), name = 'cliente_crear'),
    path('cliente/editar/<int:pk>/', ClienteUpdateView.as_view(), name = 'cliente_editar'),
    path('cliente/eliminar/<int:pk>/', ClienteDeleteView.as_view(), name = 'cliente_eliminar'),


]

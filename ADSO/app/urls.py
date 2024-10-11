from django.urls import path, include
from app.views import vista_home, GlobalLogoutView
from app.vistas.producto.views import *
from app.vistas.cliente.views import *
from app.vistas.categoria.views import *


app_name = 'app'
urlpatterns = [
    # Inicio
    path('inicio/', vista_home, name='Inicio' ),
    path('logout/', GlobalLogoutView.as_view, name='Logout' ),
    

    
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

    # urls Categoria
    path('categoria/listar/', CategoriaListView.as_view(), name= 'categoria_lista'),
    path('categoria/crear/', CategoriaCreateView.as_view(), name = 'categoria_crear'),
    path('categoria/editar/<int:pk>/', CategoriaUpdateView.as_view(), name = 'categoria_editar'),
    path('categoria/eliminar/<int:pk>/', CategoriaDeleteView.as_view(), name = 'categoria_eliminar'),
]

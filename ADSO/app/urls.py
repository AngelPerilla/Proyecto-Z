from django.urls import path
from app.views import *
from app.vistas.producto.views import *

app_name = 'app'
urlpatterns = [
    path('home/', vista_home, name= 'home'),
    path('producto/listar/', ProductoListView.as_view(), name= 'producto_lista'),
    path('producto/crear/', ProductoCreateView.as_view(), name = 'producto_crear'),
    path('producto/editar/<int:pk>/', ProductoUpdateView.as_view(), name = 'producto_editar'),
    path('producto/eliminar/<int:pk>/', ProductoDeleteView.as_view(), name = 'producto_eliminar'),
]

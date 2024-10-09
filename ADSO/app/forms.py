from django.forms import *
from app.models import Producto

class ProductoForm(ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs['autofocus'] = True
    
    class Meta:
        model = Producto
        fields = '__all__'
        widgets = {
            'nombre' : TextInput(
                attrs = {
                    'placeholder' : 'Ingrese un nombre'
                }
            ),
            'descripcion' : Textarea(
            attrs = {
                'placeholder' : 'Ingrese una descripción',
                'rows' : 3,
                'cols' : 3
            }
            )
        }
from django import forms
from django.forms import ModelForm, CharField, DecimalField
from django.core.validators import MinLengthValidator, RegexValidator, MinValueValidator
from app.models import Producto, Cliente, Categoria

class ProductoForm(ModelForm):
    categorias = Categoria.objects.all()
    choices = [(categoria.id, categoria.nombre) for categoria in categorias]

    nombre = CharField(
        label="Nombre",
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': 'Ingrese el nombre del producto',
            'autofocus': True
        }),
        validators=[
            MinLengthValidator(1, 'El nombre debe tener al menos un carácter'),
            RegexValidator(
                regex=r'^[A-Za-z\s]+$',  # Solo letras y espacios permitidos
                message='El nombre solo puede contener letras y espacios.'
            )
        ]
    )

    cantidad = DecimalField(
        label="Cantidad",
        max_digits=10, 
        decimal_places=2,
        widget=forms.NumberInput(attrs={
            'placeholder': 'Ingrese la cantidad',
        }),
        validators=[
            MinValueValidator(0.01, 'La cantidad debe ser un número positivo mayor que 0.')
        ]
    )

    precio = DecimalField(
        label="Precio",
        max_digits=10,
        decimal_places=2,
        widget=forms.NumberInput(attrs={
            'placeholder': 'Ingrese el precio',
        }),
        validators=[
            MinValueValidator(0, 'El precio debe ser un número positivo.')
        ]
    )

    class Meta:
        model = Producto
        fields = '__all__'

class ClienteForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombres'].widget.attrs['autofocus'] = True

    class Meta:
        model = Cliente
        fields = '__all__'
        widgets = {
            'nombres': forms.TextInput(attrs={
                'placeholder': 'Ingrese los nombres',
            }),
            'apellidos': forms.TextInput(attrs={
                'placeholder': 'Ingrese los apellidos',
            }),
        }

class CategoriaForm(ModelForm):
    nombre = CharField(
        label="Nombre",
        max_length=80,
        widget=forms.TextInput(attrs={
            'placeholder': 'Ingrese un nombre',
            'autofocus': True
        }),
        validators=[
            MinLengthValidator(1, 'El nombre debe tener al menos un carácter'),
            RegexValidator(
                regex=r'^[A-Za-z\s]+$',  # Solo letras y espacios permitidos
                message='El nombre solo puede contener letras y espacios.'
            )
        ]
    )

    class Meta:
        model = Categoria
        fields = '__all__'
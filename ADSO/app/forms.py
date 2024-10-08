from dataclasses import fields
from django.forms import ModelForm
from app.models import Producto

class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
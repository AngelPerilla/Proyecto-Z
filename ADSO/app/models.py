from django.db import models
from datetime import datetime

class Producto(models.Model):
    nombre = models.CharField(max_length=60, verbose_name='Nombre', default='')
    precio = models.IntegerField(default=0)
    cantidad = models.IntegerField(default=0)
    presentacion = models.CharField(max_length=100, verbose_name='Presentacion',unique=True, default='')
    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        db_table = 'Producto'
        ordering = ['id']

class Cliente(models.Model):
    nombres = models.CharField(max_length=80, verbose_name='Nombres', default='')
    apellidos = models.CharField(max_length=80, verbose_name='Apellidos', default='')
    documento = models.CharField(max_length=20, verbose_name='Documento',unique=True, default='')
    cedula_c = 'CC'
    cedula_e = 'CE'
    nit = 'NIT'
    tarjeta_i = 'TI'
    opciones_documento = {
        cedula_c: 'Cédula de ciudadanía',
        cedula_e: 'Cédula de extrangería',
        nit: 'Número de Identificación Tributaria (NIT)',
        tarjeta_i: 'Tarjeta de identidad'
    }
    tipo_documento = models.CharField(
        max_length=4,
        choices=[('','Seleccione una opción')] + list(opciones_documento.items()),
        blank=True,unique=True,
        default=''
    )
    fecha_nacimiento = models.DateField(default=datetime.now, verbose_name='Fecha de nacimiento')
    telefono = models.CharField(max_length=20, verbose_name='Teléfono',unique=True, default='')
    direccion = models.CharField(max_length=200, null=True, blank=True, verbose_name='Dirección', default='')
    def __str__(self):
        return self.nombres
    
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        db_table = 'Cliente'
        ordering = ['id']
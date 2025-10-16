# Importación de la clase base para modelos de Django
from django.db import models
from django.db.models import UniqueConstraint
from django.core.validators import MinLengthValidator, MinValueValidator
from django.utils import timezone
from django.core.exceptions import ValidationError
# ========================================================================
# Modelo: Producto
# ========================================================================
# Representa la tabla 'Producto' en la base de datos.
# Se utiliza db_column para mapear cada campo del modelo a la columna existente
# en la base de datos y evitar que Django genere nombres por defecto.
# ========================================================================

class Productos(models.Model):
    # ID del producto, clave primaria autoincremental
    IdProducto = models.AutoField(
        primary_key=True, 
        db_column='IdProducto'
    )

    # Código de barras del producto
    # CharField de hasta 100 caracteres
    # verbose_name se usa para mostrar un nombre legible en el admin de Django y en el Formulario
    CodigoDeBarras = models.CharField(
        max_length=100, 
        db_column='CodigoDeBarras', 
        verbose_name="Código de Barras",
        error_messages={'unique': 'El código de barras ingresado ya se encuentra registrado. Por favor, verifique.'}
    )

    # Valor del producto
    ValorProducto = models.IntegerField(
        db_column='ValorProducto',
        verbose_name="Valor",
        validators=[MinValueValidator(1000, message="El valor minimo de un producto es de $1000")]
    )

    # Cantidad disponible en stock
    StockProducto = models.IntegerField(
        db_column='StockProducto', 
        verbose_name="Stock",
        validators=[MinValueValidator(1, message="El Stock minimo es de 1 unidad ")]
    )

    # Nombre del producto
    NombreProducto = models.CharField(
        max_length=60, 
        db_column='NombreProducto', 
        verbose_name="Nombre del producto",
        validators=[MinLengthValidator(5, message="El nombre del producto debe tener al menos 5 caracteres.")]
    )

    # Fecha en que se registró el producto, se asigna automáticamente al crear
    FechaDeRegistroProducto = models.DateTimeField(
        auto_now_add=True, 
        db_column='FechaDeRegistroProducto'
    )

    # Marca del producto
    MarcaProducto = models.CharField(
        max_length=55, 
        db_column='MarcaProducto', 
        verbose_name="Marca",
        validators=[MinLengthValidator(4, message="La marca del producto debe tener al menos 4 caracteres")]
    )

    def validacion_fecha_de_vencimiento_futura(value):
        if value <= timezone.now().date():
            raise ValidationError('La fecha ingresada no es una fecha futura.',)
        
    # Fecha de vencimiento del producto
    FechaDeVencimiento = models.DateField(
        db_column='FechaDeVencimiento', 
        verbose_name="Fecha de vencimiento",
        validators=[
            validacion_fecha_de_vencimiento_futura
        ]
    )

    # --------------------------------------------------------------------
    # Meta información del modelo
    # --------------------------------------------------------------------
    class Meta:
        # Nombre exacto de la tabla en la base de datos
        db_table = 'Productos'
        constraints = [
            UniqueConstraint(fields=['IdProducto'], name='unique_id_producto'),
            UniqueConstraint(fields=['CodigoDeBarras'], name='unique_codigo_de_barras'),
        ]

    def __str__(self):
        return f"ID: {self.IdProducto}, NOMBRE: {self.NombreProducto}, CODIGO DE BARRAS: {self.CodigoDeBarras}, VALOR: {self.ValorProducto}, STOCK: {self.StockProducto}, MARCA: {self.MarcaProducto}, FECHA DE REGISTRO: {self.FechaDeRegistroProducto}, FECHA DE VENCIMIENTO: {self.FechaDeVencimiento}"
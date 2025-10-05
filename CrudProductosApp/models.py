# Importación de la clase base para modelos de Django
from django.db import models

# ========================================================================
# Modelo: Producto
# ========================================================================
# Representa la tabla 'Producto' en la base de datos.
# Se utiliza db_column para mapear cada campo del modelo a la columna existente
# en la base de datos y evitar que Django genere nombres por defecto.
# ========================================================================

class Producto(models.Model):
    # ID del producto, clave primaria autoincremental
    IdProducto = models.AutoField(primary_key=True, db_column='IdProducto')

    # Código de barras del producto
    # CharField de hasta 100 caracteres
    # verbose_name se usa para mostrar un nombre legible en el admin de Django y en el Formulario
    CodigoDeBarras = models.CharField(
        max_length=100, 
        db_column='CodigoDeBarras', 
        verbose_name="Código de Barras"
    )

    # Valor del producto
    Valor = models.IntegerField(db_column='ValorProducto')

    # Cantidad disponible en stock
    Stock = models.IntegerField(db_column='StockProducto')

    # Nombre del producto
    NombreProducto = models.CharField(
        max_length=60, 
        db_column='NombreProducto', 
        verbose_name="Nombre del producto"
    )

    # Fecha en que se registró el producto, se asigna automáticamente al crear
    FechaDeRegistroProducto = models.DateTimeField(
        auto_now_add=True, 
        db_column='FechaDeRegistroProducto'
    )

    # Marca del producto
    Marca = models.CharField(max_length=55, db_column='MarcaProducto')

    # Fecha de vencimiento del producto
    FechaDeVencimiento = models.DateField(
        db_column='FechaDeVencimiento', 
        verbose_name="Fecha de vencimiento"
    )

    # --------------------------------------------------------------------
    # Meta información del modelo
    # --------------------------------------------------------------------
    class Meta:
        # Nombre exacto de la tabla en la base de datos
        db_table = 'Producto'

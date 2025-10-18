from django.db import models
from django.db.models import UniqueConstraint
# Create your models here.
class CategoriaProducto(models.Model):
    IdCategoriaProducto = models.AutoField(primary_key=True, db_column='IdCategoriaProducto', verbose_name='Id Categoria Producto')
    NombreCategoria = models.CharField(max_length=100, db_column='NombreCategoria', verbose_name='Nombre de la categoria')
    Descripcion = models.CharField(max_length=500, db_column='Descripcion', verbose_name='Descripcion')

    class Meta:
        db_table = 'CategoriaProducto'
        constraints = [
            UniqueConstraint(fields=['IdCategoriaProducto'], name='unique_id_categoria_producto'),
        ]

    def __str__(self):
        return f"ID: {self.IdCategoriaProducto}, Nombre: {self.NombreCategoria}, Descripcion: {self.Descripcion}"
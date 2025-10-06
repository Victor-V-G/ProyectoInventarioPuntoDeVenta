from django.db import models

# Create your models here.
class CategoriaProducto(models.Model):
    IdCategoriaProducto = models.AutoField(primary_key=True, db_column='IdCategoriaProducto')
    NombreCategoria = models.CharField(max_length=100, db_column='NombreCategoria', verbose_name='Nombre de la categoria')
    Descripcion = models.CharField(max_length=500, db_column='Descripcion', verbose_name='Descripcion')

    class Meta:
        db_table = 'CategoriaProducto'
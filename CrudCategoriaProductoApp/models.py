from django.db import models

# Create your models here.
class CategoriaProducto(models.Model):
    IdCategoria = models.AutoField(primary_key=True, db_column='IdCategoria')
    NombreCategoria = models.CharField(max_length=55, db_column='NombreCategoria', verbose_name='Nombre')
    DescripcionCategoria = models.CharField(max_length=65, db_column='DescripcionCategoria', verbose_name='Descripcion')


class Meta:
    db_table = 'CategoriaProducto'
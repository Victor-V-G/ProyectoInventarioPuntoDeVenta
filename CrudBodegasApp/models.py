from django.db import models

# Create your models here.
class Bodegas(models.Model):
    IdBodega = models.AutoField(primary_key=True, db_column='IdBodega')
    NombreBodega = models.CharField(max_length=55, db_column='NombreBodega', verbose_name='Nombre')
    UbicacionBodega = models.CharField(max_length=65, db_column='UbicacionBodega', verbose_name='Ubicacion')


class Meta:
    db_table = 'Bodegas'
from django.db import models
from django.db.models import UniqueConstraint
# Create your models here.
class Bodegas(models.Model):
    IdBodega = models.AutoField(primary_key=True, db_column='IdBodega', verbose_name='Id Bodega')
    NombreBodega = models.CharField(max_length=55, db_column='NombreBodega', verbose_name='Nombre')
    UbicacionBodega = models.CharField(max_length=65, db_column='UbicacionBodega', verbose_name='Ubicacion')

    class Meta:
        db_table = 'Bodegas'
        constraints = [
            UniqueConstraint(fields=['IdBodega'], name='unique_id_bodega'),
        ]


  
    def __str__(self):
        return f"ID: {self.IdBodega}, Nombre: {self.NombreBodega}, Ubicacion: {self.UbicacionBodega}"
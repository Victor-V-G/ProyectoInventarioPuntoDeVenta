from django.db import models

# Create your models here.
class Cargos(models.Model):
    IdCargos = models.AutoField(primary_key=True, db_column='IdCargos')
    TipoDeCargo = models.CharField(max_length=55, db_column='TipoDeCargo', verbose_name='TipoDeCargo')
    EstadoDelCargo = models.CharField(max_length=45, db_column='EstadoDelCargo', verbose_name='EstadoDelCargo')

    class Meta:
        db_table = 'Cargos'
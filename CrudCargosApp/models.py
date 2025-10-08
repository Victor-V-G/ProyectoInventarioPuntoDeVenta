from django.db import models

# Create your models here.
class Cargos(models.Model):

    TIPO_DE_CARGO = [
        ('Gerente', 'Gerente'),
        ('Bodeguero', 'Bodeguero'),
    ]

    IdCargos = models.AutoField(primary_key=True, db_column='IdCargos')
    TipoDeCargo = models.CharField(max_length=55, choices=TIPO_DE_CARGO, db_column='TipoDeCargo', verbose_name='TipoDeCargo')
    EstadoDelCargo = models.CharField(max_length=45, db_column='EstadoDelCargo', verbose_name='EstadoDelCargo')

    class Meta:
        db_table = 'Cargos'
from django.db import models
from django.db.models import UniqueConstraint
# Create your models here.
class Cargos(models.Model):

    TIPO_DE_CARGO = [
        ('Gerente', 'Gerente'),
        ('Bodeguero', 'Bodeguero'),
    ]

    IdCargos = models.AutoField(primary_key=True, db_column='IdCargos', verbose_name='Id Cargo')
    TipoDeCargo = models.CharField(max_length=55, choices=TIPO_DE_CARGO, db_column='TipoDeCargo', verbose_name='Tipo de cargo')
    EstadoDelCargo = models.CharField(max_length=45, db_column='EstadoDelCargo', verbose_name='Estado del cargo')

    class Meta:
        db_table = 'Cargos'
        constraints = [
            UniqueConstraint(fields=['IdCargos'], name='unique_id_cargos'),
        ]


    def __str__(self):
        return f"ID: {self.IdCargos}, Tipo de Cargo: {self.TipoDeCargo}, Estado del Cargo: {self.EstadoDelCargo}"
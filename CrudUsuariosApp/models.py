from django.db import models
from django.db.models import UniqueConstraint
from django.core.validators import MinLengthValidator
from django.core.exceptions import ValidationError
import re
# Create your models here.

#se usa db_column='(tabla)' , debido a que django trata de crear su propia tabla y columnas llamada CrudEmpleadosApp_Empleados
#entonces gracias a db_column='(tabla)' , se hace referencia directa al campo de la tabla Empleados que ya estaba
#en la base de datos

class Usuarios(models.Model):

    IdUsuarios = models.AutoField(
        primary_key=True, 
        db_column='IdUsuarios'
    )

    Username = models.CharField(
        max_length=30, 
        db_column='Username',
        validators=[MinLengthValidator(5, message="El username debe tener al menos 5 caracteres")],
        error_messages={'unique': 'El username ingresado ya se encuentra ocupado, Por favor, Intentelo con otro nuevamente.'}
    )

    def validacion_password_segura(value):
        expresion = r'^(?=.*[a-zA-Z])(?=.*[0-9]).*$'
        if re.search(expresion, value):
            return value
        else:
            raise ValidationError('La password ingresada debe contener al menos 1 letra y 1 numero')

    Password = models.CharField(
        max_length=45, 
        db_column='Password',
        validators=[
            validacion_password_segura,
            MinLengthValidator(5, message="La password debe tener al menos 5 caracteres")]
    )
    
    #Aqui se llama a la tabla la cual queremos insertar/mostrar datos, esto evitando lo mencionado anteriormente
    class Meta:
        db_table = 'Usuarios'
        constraints = [
            UniqueConstraint(fields=['IdUsuarios'], name='unique_id_usuarios'),
            UniqueConstraint(fields=['Username'], name='unique_username'),
        ]
    
    def __str__(self):
        return f"ID: {self.IdUsuarios}, USERNAME: {self.Username}, PASSWORD: {self.Password}"
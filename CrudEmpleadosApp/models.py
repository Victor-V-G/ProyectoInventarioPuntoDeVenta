# Importación de la clase base para modelos de Django
from django.db import models
from django.db.models import UniqueConstraint
from django.core.validators import MinLengthValidator, MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError
import re
# ------------------------------------------------------------------------
# Modelo: Empleados
# ------------------------------------------------------------------------
# Este modelo representa la tabla 'Empleados' en la base de datos.
# Nota: Se utiliza 'db_column' para mapear cada campo del modelo a la columna
# específica existente en la base de datos. Esto evita que Django cree
# automáticamente nombres de columna como CrudEmpleadosApp_Empleados_Rut.
# ------------------------------------------------------------------------

class Empleados(models.Model):
    
    # ID del empleado, clave primaria
    # CharField: campo de texto, max_length=15
    # db_column='RutEmpleado' indica que en la base de datos la columna se llama 'RutEmpleado'
    IdEmpleado = models.AutoField(
        primary_key=True, 
        db_column='IdEmpleado'
    )

    # RUT del empleado, clave primaria
    # CharField: campo de texto, max_length=15
    # db_column='RutEmpleado' indica que en la base de datos la columna se llama 'RutEmpleado'
    def validacion_rut_real(value):
        expresion = r"^\d{7,8}-[\dK]$"
        if re.match(expresion, value):
            return value
        else:
            raise ValidationError('Ingrese un rut valido (01234567-k) con guion y sin puntos.')

    RutEmpleado = models.CharField(
        max_length=10, 
        db_column='RutEmpleado', 
        verbose_name="Rut (01234567-k)",
        validators=[validacion_rut_real],
        error_messages={'unique': 'El rut ingresado ya se encuentra registrado, Por favor, verifique.'}
    )

    # Nombre del empleado
    # CharField: campo de texto, max_length=55
    # db_column='NombreEmpleado' indica que en la base de datos la columna se llama 'NombreEmpleado'
    def validacion_nombre_y_apellido_real(value):
        expresion = r"^[a-zA-ZñÑáéíóúÁÉÍÓÚ\s]+$"
        if re.match(expresion, value):
            return value
        else:
            raise ValidationError('No se permiten numeros y caracteres especiales')

    NombreEmpleado = models.CharField(
        max_length=20, 
        db_column='NombreEmpleado', 
        verbose_name="Nombre",
        validators=[
            validacion_nombre_y_apellido_real,    
            MinLengthValidator(2, message="Por favor, ingrese un nombre real")
        ]
    )

    # Apellido del empleado
    # CharField: campo de texto, max_length=55
    # db_column='ApellidoEmpleado' indica que en la base de datos la columna se llama 'ApellidoEmpleado'
    ApellidoEmpleado = models.CharField(
        max_length=55, 
        db_column='ApellidoEmpleado', 
        verbose_name="Apellido",
        validators=[
            validacion_nombre_y_apellido_real,    
            MinLengthValidator(2, message="Por favor, ingrese un apellido real")
        ]
    )

    # Edad del empleado
    # IntegerField: campo de número entero
    # db_column='EdadEmpleado' indica que en la base de datos la columna se llama 'EdadEmpleado'
   
    EdadEmpleado = models.IntegerField(
        db_column='EdadEmpleado', 
        verbose_name="Edad",
        validators=[
            MinValueValidator(18, message="Debes tener al menos 18 años"),
            MaxValueValidator(99, message="Edad invalida, no puede tener mas de 100 años")
        ]
    )

    # Teléfono del empleado
    # IntegerField: campo de número entero
    # db_column='NumeroTelefonoEmpleado' indica que en la base de datos la columna se llama 'NumeroTelefonoEmpleado'
    NumeroTelefonoEmpleado = models.IntegerField(
        db_column='NumeroTelefonoEmpleado', 
        verbose_name="Telefono (912345678)",
        validators=[MinLengthValidator(9, message="Debes ingresar la numeracion correcta (912345678)")]
    )

    # --------------------------------------------------------------------
    # Meta información del modelo
    # --------------------------------------------------------------------
    class Meta:
        # db_table indica el nombre exacto de la tabla en la base de datos
        # Evita que Django cree una tabla con un nombre por defecto como 'CrudEmpleadosApp_Empleados'
        db_table = 'Empleados'
        constraints = [
            UniqueConstraint(fields=['IdEmpleado'], name='unique_id_empleado'),
            UniqueConstraint(fields=['RutEmpleado'], name='unique_rut_empleado'),
        ]
    # --------------------------------------------------------------------
    # MÉTODO __STR__ IMPLEMENTADO
    # --------------------------------------------------------------------
    # Devuelve una representación legible del objeto.
    # En este caso, el nombre completo del empleado.
    # --------------------------------------------------------------------
    def __str__(self):
        return f"ID: {self.IdEmpleado}, Nombre: {self.NombreEmpleado}, Apellido: {self.ApellidoEmpleado}, Rut: {self.RutEmpleado}, Edad: {self.EdadEmpleado}, Telefono: {self.NumeroTelefonoEmpleado} "
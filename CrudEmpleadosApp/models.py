# Importación de la clase base para modelos de Django
from django.db import models

# ------------------------------------------------------------------------
# Modelo: Empleados
# ------------------------------------------------------------------------
# Este modelo representa la tabla 'Empleados' en la base de datos.
# Nota: Se utiliza 'db_column' para mapear cada campo del modelo a la columna
# específica existente en la base de datos. Esto evita que Django cree
# automáticamente nombres de columna como CrudEmpleadosApp_Empleados_Rut.
# ------------------------------------------------------------------------

class Empleados(models.Model):
    # RUT del empleado, clave primaria
    # CharField: campo de texto, max_length=15
    # db_column='RutEmpleado' indica que en la base de datos la columna se llama 'RutEmpleado'
    Rut = models.CharField(max_length=15, primary_key=True, db_column='RutEmpleado')

    # Nombre del empleado
    # CharField: campo de texto, max_length=55
    # db_column='NombreEmpleado' indica que en la base de datos la columna se llama 'NombreEmpleado'
    Nombre = models.CharField(max_length=55, db_column='NombreEmpleado')

    # Apellido del empleado
    # CharField: campo de texto, max_length=55
    # db_column='ApellidoEmpleado' indica que en la base de datos la columna se llama 'ApellidoEmpleado'
    Apellido = models.CharField(max_length=55, db_column='ApellidoEmpleado')

    # Edad del empleado
    # IntegerField: campo de número entero
    # db_column='EdadEmpleado' indica que en la base de datos la columna se llama 'EdadEmpleado'
    Edad = models.IntegerField(db_column='EdadEmpleado')

    # Teléfono del empleado
    # IntegerField: campo de número entero
    # db_column='NumeroTelefonoEmpleado' indica que en la base de datos la columna se llama 'NumeroTelefonoEmpleado'
    Telefono = models.IntegerField(db_column='NumeroTelefonoEmpleado')

    # --------------------------------------------------------------------
    # Meta información del modelo
    # --------------------------------------------------------------------
    class Meta:
        # db_table indica el nombre exacto de la tabla en la base de datos
        # Evita que Django cree una tabla con un nombre por defecto como 'CrudEmpleadosApp_Empleados'
        db_table = 'Empleados'

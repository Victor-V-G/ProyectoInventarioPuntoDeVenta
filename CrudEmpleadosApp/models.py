from django.db import models

#se usa db_column='(tabla)' , debido a que django trata de crear su propia tabla y columnas llamada CrudEmpleadosApp_Empleados
#entonces gracias a db_column='(tabla)' , se hace referencia directa al campo de la tabla Empleados que ya estaba
#en la base de datos

class Empleados(models.Model):
    RutEmpleado = models.IntegerField(primary_key=True, db_column='RutEmpleado')
    NombreEmpleado = models.CharField(max_length=55, db_column='NombreEmpleado')
    ApellidoEmpleado = models.CharField(max_length=55, db_column='ApellidoEmpleado')
    EdadEmpleado = models.IntegerField(db_column='EdadEmpleado')
    NumeroTelefonoEmpleado = models.IntegerField(db_column='NumeroTelefonoEmpleado')

    #Aqui se llama a la tabla la cual queremos insertar/mostrar datos, esto evitando lo mencionado anteriormente
    class Meta:
        db_table = 'Empleados'   
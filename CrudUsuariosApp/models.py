from django.db import models

# Create your models here.

#se usa db_column='(tabla)' , debido a que django trata de crear su propia tabla y columnas llamada CrudEmpleadosApp_Empleados
#entonces gracias a db_column='(tabla)' , se hace referencia directa al campo de la tabla Empleados que ya estaba
#en la base de datos

class Usuarios(models.Model):
    IdUsuarios = models.AutoField(primary_key=True, db_column='IdUsuarios')
    Username = models.CharField(max_length=30, db_column='Username')
    Password = models.CharField(max_length=45, db_column='Password')
    
    #Aqui se llama a la tabla la cual queremos insertar/mostrar datos, esto evitando lo mencionado anteriormente
    class Meta:
        db_table = 'Usuarios'   
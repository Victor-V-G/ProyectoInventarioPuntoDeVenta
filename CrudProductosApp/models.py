from django.db import models

#se usa db_column='(tabla)' , debido a que django trata de crear su propia tabla y columnas llamada CrudEmpleadosApp_Empleados
#entonces gracias a db_column='(tabla)' , se hace referencia directa al campo de la tabla Empleados que ya estaba
#en la base de datos

class Producto(models.Model):
    IdProducto = models.IntegerField(primary_key=True, db_column='IdProducto')
    CodigoDeBarras = models.CharField(max_length=100, db_column='CodigoDeBarras')
    ValorProducto = models.IntegerField(db_column='ValorProducto')
    StockProducto = models.IntegerField(db_column='StockProducto')
    NombreProducto = models.CharField(max_length=60, db_column='NombreProducto')
    FechaDeRegistroProducto = models.DateTimeField(auto_now_add=True, db_column='FechaDeRegistroProducto')
    MarcaProducto = models.CharField(max_length=55, db_column='MarcaProducto')
    FechaDeVencimiento = models.DateField(db_column='FechaDeVencimiento')

    #Aqui se llama a la tabla la cual queremos insertar/mostrar datos, esto evitando lo mencionado anteriormente
    class Meta:
        db_table = 'Producto'   
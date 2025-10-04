from django.contrib import admin
from CrudProductosApp.models import Producto

# Register your models here.

#crear super usuario: python manage.py createsuperuser

#esto sirve para aplicarle los atributos de nuestro models previamente creado y definido,
#con esto directamente desde admin podemos realizar funciones crud hacia la base de datos
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['IdProducto', 'CodigoDeBarras', 'ValorProducto', 'StockProducto', 'NombreProducto', 'FechaDeRegistroProducto', 'MarcaProducto', 'FechaDeVencimiento']

# Register your models here.
admin.site.register(Producto)

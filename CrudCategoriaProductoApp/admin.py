from django.contrib import admin
from CrudCategoriaProductoApp.models import CategoriaProducto

# Register your models here.
class CategoriaProductoAdmin(admin.ModelAdmin):
    list_display = [
        'IdCategoriaProducto',
        'NombreCategoria', 
        'Descripcion']

admin.site.register(CategoriaProducto)
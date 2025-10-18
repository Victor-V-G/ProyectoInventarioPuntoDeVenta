from django.contrib import admin
from CrudCategoriaProductoApp.models import CategoriaProducto

# Register your models here.
class CategoriaProductoAdmin(admin.ModelAdmin):
    list_display = [
        "IdCategoriaProducto",
        "NombreCategoria", 
        "Descripcion"]
    list_filter = [
        "NombreCategoria"]
    search_fields = [
        "IdCategoriaProducto",
        "NombreCategoria"]
    list_per_page = 10

admin.site.register(CategoriaProducto, CategoriaProductoAdmin)
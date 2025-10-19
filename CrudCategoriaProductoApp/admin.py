from django.contrib import admin
from CrudCategoriaProductoApp.models import CategoriaProducto

# Register your models here.
class CategoriaProductoAdmin(admin.ModelAdmin):
    list_display = [
        "IdCategoriaProducto",
        "NombreCategoria", 
        "Descripcion",
        "Estado",
        "Observaciones"]
    list_filter = [
        "NombreCategoria",
        "Estado"]
    search_fields = [
        "IdCategoriaProducto",
        "NombreCategoria",
        "Estado"]
    list_per_page = 10

    class Media:
        js = ('js/confirmarGuardados.js',)
        
admin.site.register(CategoriaProducto, CategoriaProductoAdmin)
# Importaciones necesarias
from django.contrib import admin  # Permite registrar modelos en el panel de administración de Django
from CrudProductosApp.models import Productos  # Importa el modelo Producto

# ------------------------------------------------------------------------
# Nota para desarrollo
# ------------------------------------------------------------------------
# Para poder acceder al panel de administración y gestionar modelos, se debe crear
# un superusuario con el comando:
# python manage.py createsuperuser
# ------------------------------------------------------------------------

# ========================================================================
# Configuración personalizada del panel de administración para Productos
# ========================================================================
class ProductoAdmin(admin.ModelAdmin):
    list_display = [
        'IdProducto',
        'CodigoDeBarras', 
        'ValorProducto', 
        'StockProducto', 
        'NombreProducto', 
        'MarcaProducto', 
        'FechaDeVencimiento']
    list_filter = [ 
        "CodigoDeBarras",
        'ValorProducto', 
        "NombreProducto"]
    search_fields = [
        'IdProducto',
        'CodigoDeBarras',
        'NombreProducto',
        'MarcaProducto', ]
    list_per_page = 10


    class Media:
        js = ('js/confirmarGuardados.js',)

# ========================================================================
# Registro del modelo en el panel de administración
# ========================================================================
# Esto permite que podamos gestionar los registros de Producto directamente
# desde el panel de administración de Django (crear, leer, actualizar y eliminar)
admin.site.register(Productos, ProductoAdmin)

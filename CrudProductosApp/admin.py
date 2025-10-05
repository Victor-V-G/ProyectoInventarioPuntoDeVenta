# Importaciones necesarias
from django.contrib import admin  # Permite registrar modelos en el panel de administración de Django
from CrudProductosApp.models import Producto  # Importa el modelo Producto

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
    """
    Permite personalizar la forma en que se muestran los registros del modelo Producto
    en el panel de administración de Django.
    """
    # 'list_display' define qué columnas se mostrarán en la lista de registros en el admin
    list_display = [
        'CodigoDeBarras', 
        'ValorProducto', 
        'StockProducto', 
        'NombreProducto', 
        'MarcaProducto', 
        'FechaDeVencimiento'
    ]

# ========================================================================
# Registro del modelo en el panel de administración
# ========================================================================
# Esto permite que podamos gestionar los registros de Producto directamente
# desde el panel de administración de Django (crear, leer, actualizar y eliminar)
admin.site.register(Producto)

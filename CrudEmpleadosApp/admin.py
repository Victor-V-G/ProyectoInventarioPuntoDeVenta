# Importaciones necesarias
from django.contrib import admin  # Permite registrar modelos en el panel de administración de Django
from CrudEmpleadosApp.models import Empleados  # Importa el modelo Empleados

# ------------------------------------------------------------------------
# Nota para desarrollo
# ------------------------------------------------------------------------
# Para poder acceder al panel de administración y gestionar modelos, se debe crear
# un superusuario con el comando:
# python manage.py createsuperuser
# ------------------------------------------------------------------------

# ========================================================================
# Configuración personalizada del panel de administración para Empleados
# ========================================================================
class EmpleadoAdmin(admin.ModelAdmin):
    """
    Permite personalizar la forma en que se muestran los registros del modelo Empleados
    en el panel de administración de Django.
    """
    # 'list_display' define qué columnas se mostrarán en la lista de registros en el admin
    list_display = ['IdEmpleado','RutEmpleado', 'NombreEmpleado', 'ApellidoEmpleado', 'EdadEmpleado', 'NumeroTelefonoEmpleado']
    list_filter = ('IdEmpleado',)
    search_fields = ('Nombre', 'RutEmpleado')
    list_per_page = 10  # paginación
    empty_value_display = '— Sin dato —'

# ========================================================================
# Registro del modelo en el panel de administración
# ========================================================================
# Esto permite que podamos gestionar los registros de Empleados directamente
# desde el panel de administración de Django (crear, leer, actualizar y eliminar)
admin.site.register(Empleados)

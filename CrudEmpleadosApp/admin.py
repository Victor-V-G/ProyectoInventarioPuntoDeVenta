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
    list_display = [
        "IdEmpleado",
        "RutEmpleado", 
        "NombreEmpleado",
        "ApellidoEmpleado",
        "EdadEmpleado",
        "NumeroTelefonoEmpleado"]
    list_filter = [
        "RutEmpleado", 
        "NombreEmpleado",
        "ApellidoEmpleado"]
    search_fields = [
        "IdEmpleado",
        "RutEmpleado", 
        "NombreEmpleado",
        "ApellidoEmpleado"]
    list_per_page = 10

    class Media:
        js = ('js/confirmarGuardados.js',)

# ========================================================================
# Registro del modelo en el panel de administración
# ========================================================================
# Esto permite que podamos gestionar los registros de Empleados directamente
# desde el panel de administración de Django (crear, leer, actualizar y eliminar)
admin.site.register(Empleados, EmpleadoAdmin)

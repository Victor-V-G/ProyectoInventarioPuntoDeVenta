from django.contrib import admin
from CrudEmpleadosApp.models import Empleados

#crear super usuario: python manage.py createsuperuser


#esto sirve para aplicarle los atributos de nuestro models previamente creado y definido,
#con esto directamente desde admin podemos realizar funciones crud hacia la base de datos
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ['RutEmpleado', 'NombreEmpleado', 'ApellidoEmpleado', 'EdadEmpleado', 'NumeroTelefonoEmpleado']

# Register your models here.
admin.site.register(Empleados)

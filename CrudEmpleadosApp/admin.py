from django.contrib import admin
from CrudEmpleadosApp.models import Empleados

#crear super usuario: python manage.py createsuperuser

# Register your models here.
admin.site.register(Empleados)

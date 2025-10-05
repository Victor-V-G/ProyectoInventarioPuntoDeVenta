from django.contrib import admin
from CrudUsuariosApp.models import Usuarios

#crear super usuario: python manage.py createsuperuser

#esto sirve para aplicarle los atributos de nuestro models previamente creado y definido,
#con esto directamente desde admin podemos realizar funciones crud hacia la base de datos

#Campos en models con AutoIncrement no se colocan en list_display

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['Username', 'Password']


# Register your models here.
admin.site.register(Usuarios)
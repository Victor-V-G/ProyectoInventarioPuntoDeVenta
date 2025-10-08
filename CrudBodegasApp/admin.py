from django.contrib import admin
from CrudBodegasApp.models import Bodegas

# Register your models here.
class BodegaAdmin(admin.ModelAdmin):
    list_display = [
        'IdBodega',
        'NombreBodega', 
        'UbicacionBodega']

admin.site.register(Bodegas)
from django.contrib import admin
from CrudCargosApp.models import Cargos

# Register your models here.
class BodegaAdmin(admin.ModelAdmin):
    list_display = [
        'IdCargos',
        'TipoDeCargo', 
        'EstadoDelCargo']

admin.site.register(Cargos)
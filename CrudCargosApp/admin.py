from django.contrib import admin
from CrudCargosApp.models import Cargos

# Register your models here.
class CargoAdmin(admin.ModelAdmin):
    list_display = [
        "IdCargos",
        "TipoDeCargo", 
        "EstadoDelCargo",
        "DescripcionDelCargo",
        "SueldoBase"]
    list_filter = [
        "TipoDeCargo", 
        "EstadoDelCargo",
        "SueldoBase"]
    search_fields = [
        "IdCargos",
        "TipoDeCargo", 
        "EstadoDelCargo",
        "SueldoBase"]
    list_per_page = 10

    class Media:
        js = ('js/confirmarGuardados.js',)

admin.site.register(Cargos, CargoAdmin)
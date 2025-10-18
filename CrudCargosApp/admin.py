from django.contrib import admin
from CrudCargosApp.models import Cargos

# Register your models here.
class CargoAdmin(admin.ModelAdmin):
    list_display = [
        "IdCargos",
        "TipoDeCargo", 
        "EstadoDelCargo"]
    list_filter = [
        "TipoDeCargo", 
        "EstadoDelCargo"]
    search_fields = [
        "IdCargos",
        "TipoDeCargo", 
        "EstadoDelCargo"]
    list_per_page = 10

    class Media:
        js = ('js/confirmarGuardados.js',)

admin.site.register(Cargos, CargoAdmin)
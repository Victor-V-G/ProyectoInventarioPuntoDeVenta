from django.contrib import admin
from CrudBodegasApp.models import Bodegas

# Register your models here.
class BodegaAdmin(admin.ModelAdmin):
    list_display = [
        "IdBodega",
        "NombreBodega", 
        "UbicacionBodega",
        "EstadoBodega",
        "ObservacionesBodega"]
    list_filter = [
        "NombreBodega", 
        "UbicacionBodega",
        "EstadoBodega"]
    search_fields = [
        "IdBodega",
        "NombreBodega", 
        "UbicacionBodega",
        "EstadoBodega"]
    list_per_page = 10
    
    class Media:
        js = ('js/confirmarGuardados.js',)

admin.site.register(Bodegas, BodegaAdmin)
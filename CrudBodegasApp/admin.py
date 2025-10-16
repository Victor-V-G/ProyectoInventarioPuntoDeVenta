from django.contrib import admin
from CrudBodegasApp.models import Bodegas

# Register your models here.
class BodegaAdmin(admin.ModelAdmin):
    list_display = [
        "IdBodega",
        "NombreBodega", 
        "UbicacionBodega"]
    list_filter = [
        "NombreBodega", 
        "UbicacionBodega"]
    search_fields = [
        "IdBodega",
        "NombreBodega", 
        "UbicacionBodega"]
    list_per_page = 10

admin.site.register(Bodegas, BodegaAdmin)
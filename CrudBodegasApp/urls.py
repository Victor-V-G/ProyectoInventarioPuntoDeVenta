from django.contrib import admin
from django.urls import path
from CrudBodegasApp import views
from CrudBodegasApp.forms import BodegaRegistracionForm
# Lista de rutas para la aplicación CrudBodegaApp
urlpatterns = [
    path('admin/', admin.site.urls),
    path('crud-bodegas/', views.bodegasData),
    path('crud-bodegas/registro-bodega/', views.bodegasRegistracionView),
    path('crud-bodegas/actualizar-bodega/<int:IdBodega>', views.actualizarBodega),
    path('crud-bodegas/eliminar-bodega/<int:IdBodega>', views.eliminarBodega, name='eliminar-bodega'),

    #Confirmacion Eliminar
    path('crud-bodegas/confirmar-eliminar/<int:IdBodega>', views.confirmarEliminar),

    #Detalle
    path('crud-bodegas/detalle-bodega/<int:IdBodega>', views.detalleBodega),
]

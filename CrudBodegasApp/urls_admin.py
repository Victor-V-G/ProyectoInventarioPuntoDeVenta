from django.urls import path
from CrudBodegasApp import views


urlpatterns = [

    path('crud-bodegas/', views.bodegasData, name='admin-crud-bodega'),

    path('crud-bodegas/registro-bodega/', views.bodegasRegistracionView, name='admin-registrar-bodega'),

    path('crud-bodegas/detalle-bodega/<int:IdBodega>', views.detalleBodega, name='admin-detalle-bodega'),

    path('crud-bodegas/actualizar-bodega/<int:IdBodega>', views.actualizarBodega, name='admin-actualizar-bodega'),

    path('crud-bodegas/confirmar-eliminar/<int:IdBodega>', views.confirmarEliminar, name='admin-confirmar-eliminar-bodega'),

    path('crud-bodegas/eliminar-bodega/<int:IdBodega>', views.eliminarBodega, name='admin-eliminar-bodega'),

]
from django.urls import path
from CrudBodegasApp import views


urlpatterns = [

    path('crud-bodegas/', views.bodegasData, name='crud-bodega'),

    path('crud-bodegas/registro-bodega/', views.bodegasRegistracionView, name='registro-bodega'),

    path('crud-bodegas/detalle-bodega/<int:IdBodega>', views.detalleBodega, name='detalle-bodega'),

    path('crud-bodegas/actualizar-bodega/<int:IdBodega>', views.actualizarBodega, name='actualizar-bodega'),

    path('crud-bodegas/confirmar-eliminar/<int:IdBodega>', views.confirmarEliminar, name='confirmar-eliminar-bodega'),

    path('crud-bodegas/eliminar-bodega/<int:IdBodega>', views.eliminarBodega, name='eliminar-bodega'),

]

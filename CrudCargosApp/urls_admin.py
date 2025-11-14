from django.urls import path
from CrudCargosApp import views

# Lista de rutas para la aplicación CrudCargoApp
urlpatterns = [

    path('crud-cargos/', views.cargosData, name='admin-crud-cargo'),

    path('crud-cargos/registro-cargo/', views.cargosRegistracionView, name='admin-registrar-cargo'),

    path('crud-cargos/detalle-cargo/<int:IdCargos>', views.detalleCargo, name='admin-detalle-cargo'),

    path('crud-cargos/actualizar-cargo/<int:IdCargos>', views.actualizarCargo, name='admin-actualizar-cargo'),

    path('crud-cargos/confirmar-eliminar/<int:IdCargos>', views.confirmarEliminar, name='admin-confirmar-eliminar-cargo'),

    path('crud-cargos/eliminar-cargo/<int:IdCargos>', views.eliminarCargo, name='admin-eliminar-cargo'),

]

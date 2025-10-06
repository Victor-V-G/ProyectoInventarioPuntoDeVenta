from django.contrib import admin
from django.urls import path
from CrudCargosApp import views
from CrudCargosApp.forms import CargoRegistracionForm
# Lista de rutas para la aplicación CrudCargoApp
urlpatterns = [
    path('admin/', admin.site.urls),
    path('crud-cargos/', views.cargosData),
    path('crud-cargos/registro-cargo/', views.cargosRegistracionView),
    path('crud-cargos/actualizar-cargo/<int:IdCargos>', views.actualizarCargo),
    path('crud-cargos/eliminar-cargo/<int:IdCargos>', views.eliminarCargo)
]

from django.contrib import admin
from django.urls import path, include
from AdminHomeApp.views import renderAdminHome  # Importa la view que renderiza el home del administrador
from CrudEmpleadosApp import views  # Importa views de la app CrudEmpleadosApp
from CrudUsuariosApp import views  # Importa views de la app CrudUsuariosApp
from CrudProductosApp import views  # Importa views de la app CrudProductosApp
from CrudCategoriaProductoApp import views  # Importa views de la app CrudCategoriasApp
from CrudBodegasApp import views  # Importa views de la app CrudBodegaApp
from CrudCargosApp import views  # Importa views de la app CrudBodegaApp

# Lista principal de rutas del proyecto
urlpatterns = [

    path('', renderAdminHome, name='adminhome'),

    path("", include("CrudEmpleadosApp.urls_admin")),

    path("", include("CrudUsuariosApp.urls_admin")),

    path("", include("CrudCargosApp.urls_admin")),

    path("", include("CrudProductosApp.urls_admin")),

    path("", include("CrudBodegasApp.urls_admin")),

    path("", include("CrudCategoriaProductoApp.urls_admin")),

    path("", include("AuditoriaApp.urls")),
]

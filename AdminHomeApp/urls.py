from django.contrib import admin
from django.urls import path, include
from AdminHomeApp.views import renderAdminHome  # Importa la view que renderiza el home del administrador
from CrudEmpleadosApp import views  # Importa views de la app CrudEmpleadosApp
from CrudUsuariosApp import views  # Importa views de la app CrudUsuariosApp
from CrudProductosApp import views  # Importa views de la app CrudProductosApp
from CrudCategoriasApp import views  # Importa views de la app CrudCategoriasApp
from CrudBodegaApp import views  # Importa views de la app CrudBodegaApp

# Lista principal de rutas del proyecto
urlpatterns = [
    # Ruta para el panel de administración de Django
    # Acceder a /admin/ abre el panel de administración estándar de Django
    path('admin/', admin.site.urls),

    # Ruta raíz del home de administrador
    # Al acceder a la raíz (''), se ejecuta la view renderAdminHome
    path('', renderAdminHome),

    # Rutas para CRUD de empleados
    # Todas las URLs definidas en CrudEmpleadosApp.urls se incluyen bajo /crudempleados/
    path("", include("CrudEmpleadosApp.urls")),

    # Rutas para CRUD de usuarios
    # Todas las URLs definidas en CrudUsuariosApp.urls se incluyen bajo /crudusuarios/
    path("crudusuarios/", include("CrudUsuariosApp.urls")),

    # Rutas para CRUD de productos
    # Todas las URLs definidas en CrudProductosApp.urls se incluyen bajo /crudproductos/
    path("", include("CrudProductosApp.urls")),

    # Rutas para CRUD de categorías
    # Todas las URLs definidas en CrudCategoriasApp.urls se incluyen bajo /crudcategorias/
    path("crudcategorias/", include("CrudCategoriasApp.urls")),

    # Rutas para CRUD de bodegas
    # Todas las URLs definidas en CrudBodegaApp.urls se incluyen bajo /crudbodegas/
    path("crudbodegas/", include("CrudBodegaApp.urls"))
]

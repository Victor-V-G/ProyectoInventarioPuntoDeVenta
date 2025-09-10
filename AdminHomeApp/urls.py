from django.contrib import admin
from django.urls import path, include
from AdminHomeApp.views import renderAdminHome
from CrudEmpleadosApp import views 
from CrudUsuariosApp import views
from CrudProductosApp import views
from CrudCategoriasApp import views
from CrudBodegaApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', renderAdminHome),
    path("crudempleados/", include("CrudEmpleadosApp.urls")),
    path("crudusuarios/", include("CrudUsuariosApp.urls")),
    path("crudproductos/", include("CrudProductosApp.urls")),
    path("crudcategorias/", include("CrudCategoriasApp.urls")),
    path("crudbodegas/", include("CrudBodegaApp.urls"))
    
]
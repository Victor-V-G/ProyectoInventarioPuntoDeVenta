from django.contrib import admin
from django.urls import path, include
from AdminHomeApp.views import renderAdminHome
from CrudEmpleadosApp import views 
from CrudUsuariosApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', renderAdminHome),
    path("crudempleados/", include("CrudEmpleadosApp.urls")),
    path("crudusuarios/", include("CrudUsuariosApp.urls")),
]
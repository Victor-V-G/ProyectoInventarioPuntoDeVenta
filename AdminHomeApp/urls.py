from django.contrib import admin
from django.urls import path, include
from CrudEmpleadosApp import views as CrudEmpleadosApp

urlpatterns = [
    path('admin/', admin.site.urls),
    path("CrudEmpleadosApp", include('CrudEmpleadosApp.urls'))
]
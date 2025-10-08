# Importaciones necesarias
from django.contrib import admin  # Permite usar el panel de administración de Django
from django.urls import path       # Función para definir rutas URL
from CrudEmpleadosApp import views  # Importa las vistas definidas en la app CrudEmpleadosApp
from CrudEmpleadosApp.forms import EmpleadoRegistrationForm  # Import opcional si se usa el formulario directamente

# ========================================================================
# Lista de rutas URL de la aplicación CrudEmpleadosApp
# ========================================================================
urlpatterns = [
    # --------------------------------------------------------------------
    # Ruta para el panel de administración de Django
    # --------------------------------------------------------------------
    # Al acceder a http://<tu_dominio>/admin/ se abre el panel predeterminado de Django
    path('admin/', admin.site.urls),

    # --------------------------------------------------------------------
    # Rutas relacionadas con los modelos
    # --------------------------------------------------------------------
    # Muestra todos los empleados en la tabla
    # http://<tu_dominio>/crud-empleado/
    path('crud-empleado/', views.empleadosData),

    # --------------------------------------------------------------------
    # Rutas relacionadas con formularios
    # --------------------------------------------------------------------
    # Registro de un nuevo empleado mediante formulario
    # http://<tu_dominio>/crud-empleado/registro-empleado/
    path('crud-empleado/registro-empleado/', views.empleadoRegistrationView),

    # --------------------------------------------------------------------
    # Ruta para actualizar un empleado existente
    # --------------------------------------------------------------------
    # El parámetro <int:Rut> indica que se espera un número entero correspondiente al RUT del empleado
    # http://<tu_dominio>/crud-empleado/actualizar-empleado/12345678
    path('crud-empleado/actualizar-empleado/<int:IdEmpleado>', views.actualizarEmpleado),

    # --------------------------------------------------------------------
    # Ruta para eliminar un empleado
    # --------------------------------------------------------------------
    # Similar al anterior, <int:Rut> indica el RUT del empleado a eliminar
    # http://<tu_dominio>/crud-empleado/eliminar-empleado/12345678
    path('crud-empleado/eliminar-empleado/<int:IdEmpleado>', views.eliminarEmpleado)
]

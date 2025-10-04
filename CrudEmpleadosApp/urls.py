from django.contrib import admin
from django.urls import path
from CrudEmpleadosApp.views import renderCrudEmpleados  # Importa la view que muestra el listado de empleados
from CrudEmpleadosApp.views import renderTemplateFormularioAgregarEmpleado  # Importa la view que muestra el formulario para agregar un empleado
from CrudEmpleadosApp import views
# Lista de rutas para la aplicación CrudEmpleadosApp
urlpatterns = [
    # Ruta para el panel de administración de Django
    # Cuando accedes a /admin/ se abre el admin predeterminado de Django
    path('admin/', admin.site.urls),

    # Ruta raíz de la app CrudEmpleadosApp ('/crudempleados/')
    # Al acceder a la raíz de CrudEmpleadosApp, se ejecuta la view renderCrudEmpleados
    path('', renderCrudEmpleados),

    # Ruta para agregar un nuevo empleado
    # Al acceder a /crudempleados/agregar-empleado/, se ejecuta la view renderTemplateFormularioAgregarEmpleado
    path('agregar-empleado/', renderTemplateFormularioAgregarEmpleado),

    path('empleados-models/', views.empleadosData)
]

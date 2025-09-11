from django.contrib import admin
from django.urls import path
from CrudEmpleadosApp.views import renderCrudEmpleados
from CrudEmpleadosApp.views import renderTemplateFormularioAgregarEmpleado

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', renderCrudEmpleados),
    path('agregar-empleado/', renderTemplateFormularioAgregarEmpleado),
]
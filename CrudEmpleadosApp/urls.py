from django.contrib import admin
from django.urls import path
from CrudEmpleadosApp.views import renderCrudEmpleados


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', renderCrudEmpleados),
]
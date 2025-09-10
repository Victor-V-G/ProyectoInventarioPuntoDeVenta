from django.urls import path
from CrudProductosApp.views import renderTemplateCrudProductos
from CrudProductosApp.views import renderTemplateAccionARealizarProducto
from CrudProductosApp.views import renderTemplateFormularioAgregarProducto

urlpatterns = [
    path('', renderTemplateCrudProductos),
    path('accion-a-realizar-producto/', renderTemplateAccionARealizarProducto),
    path('accion-a-realizar-producto/agregar-producto', renderTemplateFormularioAgregarProducto)
]
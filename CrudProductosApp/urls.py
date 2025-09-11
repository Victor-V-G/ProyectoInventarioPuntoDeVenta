from django.urls import path
from CrudProductosApp.views import renderTemplateCrudProductos
from CrudProductosApp.views import renderTemplateFormularioAgregarProducto

urlpatterns = [
    path('', renderTemplateCrudProductos),
    path('agregar-producto/', renderTemplateFormularioAgregarProducto)
]
from django.urls import path
from CrudBodegaApp.views import renderTemplateCrudBodega
from CrudBodegaApp.views import renderTemplateAccionProductoABodega
from CrudBodegaApp.views import renderTemplateFormularioBodega

urlpatterns = [
    path('', renderTemplateCrudBodega),
    path('accion-producto-a-bodega/', renderTemplateAccionProductoABodega),
    path('accion-producto-a-bodega/formulario-bodega', renderTemplateFormularioBodega)
]
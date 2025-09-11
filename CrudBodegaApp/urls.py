from django.urls import path
from CrudBodegaApp.views import renderTemplateCrudBodega  # Importa la view que muestra el listado de bodegas
from CrudBodegaApp.views import renderTemplateAccionProductoABodega  # Importa la view para realizar acción de producto a bodega
from CrudBodegaApp.views import renderTemplateFormularioBodega  # Importa la view que muestra el formulario para agregar bodega

# Lista de rutas para la aplicación CrudBodegaApp
urlpatterns = [
    # Ruta raíz de la app ('/crudbodegas/')
    # Al acceder a la raíz de CrudBodegaApp, se ejecuta la view renderTemplateCrudBodega
    path('', renderTemplateCrudBodega),

    # Ruta para seleccionar la acción a realizar con un producto en bodega
    # Al acceder a /crudbodegas/accion-producto-a-bodega/, se ejecuta la view renderTemplateAccionProductoABodega
    path('accion-producto-a-bodega/', renderTemplateAccionProductoABodega),

    # Ruta para mostrar el formulario de agregar producto a una bodega
    # Al acceder a /crudbodegas/accion-producto-a-bodega/formulario-bodega, se ejecuta la view renderTemplateFormularioBodega
    path('accion-producto-a-bodega/formulario-bodega', renderTemplateFormularioBodega),
]

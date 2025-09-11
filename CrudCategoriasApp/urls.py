from django.urls import path
from CrudCategoriasApp.views import renderTemplateCrudCategorias  # Importa la view que muestra el listado de categorías
from CrudCategoriasApp.views import renderTemplateFormularioCategoria  # Importa la view que muestra el formulario para agregar una categoría

# Lista de rutas para la aplicación CrudCategoriasApp
urlpatterns = [
    # Ruta raíz de la app ('/crudcategorias/')
    # Al acceder a la raíz de CrudCategoriasApp, se ejecuta la view renderTemplateCrudCategorias
    path('', renderTemplateCrudCategorias),

    # Ruta para agregar una nueva categoría
    # Al acceder a /crudcategorias/formulario-categoria/, se ejecuta la view renderTemplateFormularioCategoria
    path('formulario-categoria/', renderTemplateFormularioCategoria),
]

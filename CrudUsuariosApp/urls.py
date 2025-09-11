from django.urls import path
from CrudUsuariosApp.views import renderTemplateCrudUsuario  # Importa la view que muestra el listado de usuarios
from CrudUsuariosApp.views import renderTemplateFormularioAgregarUsuario  # Importa la view que muestra el formulario para agregar un usuario

# Lista de rutas para la aplicación CrudUsuariosApp
urlpatterns = [
    # Ruta raíz de la app ('/crudusuarios/')
    # Al acceder a la raíz de CrudUsuariosApp, se ejecuta la view renderTemplateCrudUsuario
    path('', renderTemplateCrudUsuario),

    # Ruta para agregar un nuevo usuario
    # Al acceder a /crudusuarios/agregar-usuario/, se ejecuta la view renderTemplateFormularioAgregarUsuario
    path('agregar-usuario/', renderTemplateFormularioAgregarUsuario)
]

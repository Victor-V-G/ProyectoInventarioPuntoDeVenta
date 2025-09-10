from django.urls import path
from CrudUsuariosApp.views import renderTemplateCrudUsuario
from CrudUsuariosApp.views import renderTemplateAccionARealizarUsuario
from CrudUsuariosApp.views import renderTemplateFormularioAgregarUsuario


urlpatterns = [
    path('', renderTemplateCrudUsuario),
    path('accion-a-realizar-usuario/', renderTemplateAccionARealizarUsuario),
    path('accion-a-realizar-usuario/agregar-usuario/', renderTemplateFormularioAgregarUsuario)
]
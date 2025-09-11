from django.urls import path
from CrudUsuariosApp.views import renderTemplateCrudUsuario
from CrudUsuariosApp.views import renderTemplateFormularioAgregarUsuario


urlpatterns = [
    path('', renderTemplateCrudUsuario),
    path('agregar-usuario/', renderTemplateFormularioAgregarUsuario)
]
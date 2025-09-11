from django.urls import path
from CrudCategoriasApp.views import renderTemplateCrudCategorias
from CrudCategoriasApp.views import renderTemplateFormularioCategoria

urlpatterns = [
    path('', renderTemplateCrudCategorias),
    path('formulario-categoria/', renderTemplateFormularioCategoria),
]
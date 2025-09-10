from django.urls import path
from CrudCategoriasApp.views import renderTemplateCrudCategorias

urlpatterns = [
    path('', renderTemplateCrudCategorias),
]
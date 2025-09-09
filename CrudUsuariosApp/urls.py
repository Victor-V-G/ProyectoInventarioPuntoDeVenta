from django.urls import path
from CrudUsuariosApp.views import renderTemplateCrudUsuario

urlpatterns = [
    path('', renderTemplateCrudUsuario)
]
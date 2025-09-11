from django.urls import path, include
from HomeApp.views import renderTemplateHome
from CrudProductosApp import views
from CrudCategoriasApp import views
from CrudBodegaApp import views

urlpatterns = [
    path('', renderTemplateHome),
    path('crudproductos/', include("CrudProductosApp.urls")),
    path('crudcategorias/', include("CrudCategoriasApp.urls")),
    path('crudbodegas/', include("CrudBodegaApp.urls")),
]
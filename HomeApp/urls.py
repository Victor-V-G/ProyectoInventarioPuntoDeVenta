from django.urls import path, include
from HomeApp.views import renderTemplateHome
from CrudProductosApp import views
from CrudCategoriasApp import views
from CrudBodegaApp import views

urlpatterns = [
    path('', renderTemplateHome),
    path('crudproductos/', include("CrudProductosApp.urls")),
    path('crudcategorias/', include("CrudCategoriasApp.urls")),
    path('crudbodega/', include("CrudBodegaApp.urls")),
]
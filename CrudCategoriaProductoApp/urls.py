from django.contrib import admin
from django.urls import path
from CrudCategoriaProductoApp import views
from CrudCategoriaProductoApp.forms import CategoriaProductoRegistracionForm
# Lista de rutas para la aplicación CrudCategoiaApp
urlpatterns = [
    path('admin/', admin.site.urls),
    path('crud-categoriaProducto/', views.categoriaProductoData),
    path('crud-categoriaProducto/registro-categoriaProducto/', views.categoriaProductoRegistracionView),
    path('crud-categoriaProducto/actualizar-categoriaProducto/<int:IdCategoriaProducto>', views.actualizarCategoriaProducto),
    path('crud-categoriaProducto/eliminar-categoriaProducto/<int:IdCategoriaProducto>', views.eliminarCategoriaProducto)
]

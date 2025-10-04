from django.urls import path
from CrudProductosApp.views import renderTemplateCrudProductos  # Importa la view que muestra el listado de productos
from CrudProductosApp.views import renderTemplateFormularioAgregarProducto  # Importa la view que muestra el formulario para agregar un producto
from CrudProductosApp import views

# Lista de rutas para la aplicación CrudProductosApp
urlpatterns = [
    # Ruta raíz de la app ('/crudproductos/')
    # Al acceder a la raíz de CrudProductosApp, se ejecuta la view renderTemplateCrudProductos
    path('', renderTemplateCrudProductos),

    # Ruta para agregar un nuevo producto
    # Al acceder a /crudproductos/agregar-producto/, se ejecuta la view renderTemplateFormularioAgregarProducto
    path('agregar-producto/', renderTemplateFormularioAgregarProducto),

    #Models Ruta
    path('producto-models/', views.productoData)

]

# Importaciones necesarias
from django.urls import path  # Función para definir rutas URL
from CrudProductosApp import views  # Importa las vistas de la app CrudProductosApp

# ========================================================================
# Lista de rutas URL de la aplicación CrudProductosApp
# ========================================================================
urlpatterns = [
    # --------------------------------------------------------------------
    # Ruta para mostrar todos los productos
    # --------------------------------------------------------------------
    # http://<tu_dominio>/crud-producto/
    path('crud-producto/', views.productoData),

    # --------------------------------------------------------------------
    # Ruta para registrar un nuevo producto mediante formulario
    # --------------------------------------------------------------------
    # http://<tu_dominio>/crud-producto/registro-producto/
    path('crud-producto/registro-producto/', views.productoRegistrationView),

    # --------------------------------------------------------------------
    # Ruta para actualizar un producto existente
    # --------------------------------------------------------------------
    # <int:IdProducto> indica que se espera un número entero correspondiente al ID del producto
    # http://<tu_dominio>/crud-producto/actualizar-producto/1
    path('crud-producto/actualizar-producto/<int:IdProducto>', views.actualizarProducto),

    # --------------------------------------------------------------------
    # Ruta para eliminar un producto
    # --------------------------------------------------------------------
    # <int:IdProducto> indica que se espera un número entero correspondiente al ID del producto
    # http://<tu_dominio>/crud-producto/eliminar-producto/1
    path('crud-producto/eliminar-producto/<int:IdProducto>', views.eliminarProducto)
]

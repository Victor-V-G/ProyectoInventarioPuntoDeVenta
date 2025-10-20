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
    path('crud-productos/', views.productosData),

    # --------------------------------------------------------------------
    # Ruta para registrar un nuevo producto mediante formulario
    # --------------------------------------------------------------------
    # http://<tu_dominio>/crud-producto/registro-producto/
    path('crud-productos/registro-producto/', views.productosRegistrationView),

    # --------------------------------------------------------------------
    # Ruta para actualizar un producto existente
    # --------------------------------------------------------------------
    # <int:IdProducto> indica que se espera un número entero correspondiente al ID del producto
    # http://<tu_dominio>/crud-producto/actualizar-producto/1
    path('crud-productos/actualizar-producto/<int:IdProducto>', views.actualizarProducto),

    # --------------------------------------------------------------------
    # Ruta para eliminar un producto
    # --------------------------------------------------------------------
    # <int:IdProducto> indica que se espera un número entero correspondiente al ID del producto
    # http://<tu_dominio>/crud-producto/eliminar-producto/1
    path('crud-productos/eliminar-producto/<int:IdProducto>', views.eliminarProducto, name='eliminar-producto'),

    #Confirmacion Eliminar
    path('crud-productos/confirmar-eliminar/<int:IdProducto>', views.confirmarEliminar),

    #Detalle
    path('crud-productos/detalle-producto/<int:IdProducto>', views.detalleProducto),
]

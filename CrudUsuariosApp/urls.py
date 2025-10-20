from django.urls import path
from CrudUsuariosApp import views

# Lista de rutas para la aplicación CrudUsuariosApp
urlpatterns = [

    #Models
    path('crud-usuarios/', views.usuariosData),

    #Form
    path('crud-usuarios/registro-usuario/', views.usuariosRegistrationView),

    #Actualizar
    path('crud-usuarios/actualizar-usuario/<int:IdUsuarios>', views.actualizarUsuario),

    #Confirmacion Eliminar
    path('crud-usuarios/confirmar-eliminar/<int:IdUsuarios>', views.confirmarEliminar),

    #Eliminar
    path('crud-usuarios/confirmar-eliminar/eliminar-usuario/<int:IdUsuarios>', views.eliminarUsuario),

    #Detalle
    path('crud-usuarios/detalle-usuario/<int:IdUsuarios>', views.detalleUsuario),
]

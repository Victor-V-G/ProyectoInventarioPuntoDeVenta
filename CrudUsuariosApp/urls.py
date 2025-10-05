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

    #Eliminar
    path('crud-usuarios/eliminar-usuario/<int:IdUsuarios>', views.eliminarUsuario)
]

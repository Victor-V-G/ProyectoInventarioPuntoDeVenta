from django.urls import path
from LoginApp.views import renderlogin  # Importa la view que renderiza el template de login

# Lista de rutas para la aplicación LoginApp
urlpatterns = [
    # Ruta raíz de LoginApp ('/')
    # Cuando el usuario accede a la raíz de la aplicación, se ejecuta la view renderlogin
    path('', renderlogin)
]

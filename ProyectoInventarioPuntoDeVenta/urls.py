"""
URL configuration for ProyectoInventarioPuntoDeVenta project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from LoginApp.views import renderlogin as Login
from AdminHomeApp import views as AdminHomeApp

urlpatterns = [
    path('admin/', admin.site.urls),

    #RUTA DEL LOGIN
    path('', include('LoginApp.urls')),

    #RUTA DEL HOME ADMIN
    path('adminhome/', include('AdminHomeApp.urls')),

    #RUTA DEL HOME
    path('home/', include("HomeApp.urls")),
]


from django.urls import path
from AuditoriaApp import views

urlpatterns = [
    
    path('auditorias/', views.AuditoriaData, name='auditorias')

]

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


#ESTA VIEW PERMITE RENDERIZAR EL TEMPLATES DE LOGIN
def renderlogin(request):
    # Renderiza y devuelve el template de login al navegador
    return render(request, 'templateLogin/login.html')
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


#ESTA VIEW PERMITE RENDERIZAR EL TEMPLATES DE LOGIN
def renderlogin(request):
    return render(request, 'templateLogin/login.html')
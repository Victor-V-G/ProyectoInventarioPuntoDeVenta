from django.shortcuts import render
from LoginApp.decorators import login_requerido

# Create your views here.
#RENDER PARA EL TEMPLATE DEL HOME
@login_requerido
def renderTemplateHome (request):
    return render(request, "templateHome/home.html")
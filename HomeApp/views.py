from django.shortcuts import render
from LoginApp.decorators import login_requerido
from CrudUsuariosApp.models import Usuarios

# Create your views here.
#RENDER PARA EL TEMPLATE DEL HOME
@login_requerido
def renderTemplateHome (request):

    UsuarioLogeado = request.session.get("Usuario_Username")
    UsuarioObtenido = Usuarios.objects.filter(Username=UsuarioLogeado)

    data = {'Usuario': UsuarioObtenido
            }
    return render(request, "templateHome/home.html", data)
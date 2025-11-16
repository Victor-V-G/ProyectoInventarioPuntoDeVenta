from django.shortcuts import render
from LoginApp.decorators import login_requerido
from CrudUsuariosApp.models import Usuarios


# Create your views here.
@login_requerido
def renderAdminHome(request):
    UsuarioLogeado = request.session.get('Usuario_Username')
    UsuarioObjeto = Usuarios.objects.filter(Username=UsuarioLogeado)

    data = {'Usuario': UsuarioObjeto}
    
    return render(request, 'templateAdminHome/adminhome.html', data)



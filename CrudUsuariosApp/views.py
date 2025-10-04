from django.shortcuts import render
from CrudUsuariosApp.models import Usuarios

# Create your views here.
def renderTemplateCrudUsuario (request):
    return render(request, 'templateCrudUsuario/crudusuario.html')


def renderTemplateFormularioAgregarUsuario (request):
    return render(request, 'templateCrudUsuario/formulario-usuario.html')

#Models
def usuariosData(request):
    usuarios = Usuarios.objects.all()
    data = {'Usuarios' : usuarios}
    return render(request, 'templateCrudUsuario/usuarios-models.html', data)
from django.shortcuts import render

# Create your views here.
def renderTemplateCrudUsuario (request):
    return render(request, 'templateCrudUsuario/crudusuario.html')


def renderTemplateAccionARealizarUsuario (request):
    return render(request, 'templateCrudUsuario/accion-a-realizar-usuario.html')


def renderTemplateFormularioAgregarUsuario (request):
    return render(request, 'templateCrudUsuario/formulario-usuario.html')

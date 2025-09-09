from django.shortcuts import render

# Create your views here.
def renderTemplateCrudUsuario (request):
    return render(request, 'templateCrudUsuario/crudusuario.html')
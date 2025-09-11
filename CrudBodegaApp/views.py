from django.shortcuts import render

# Create your views here.
def renderTemplateCrudBodega (request):
    return render(request, "templateCrudBodega/crudbodega.html")


def renderTemplateAccionProductoABodega (request):
    return render(request, "templateCrudBodega/accion-producto-a-bodega.html")


def renderTemplateFormularioBodega (request):
    return render(request, "templateCrudBodega/formulario-bodega.html")
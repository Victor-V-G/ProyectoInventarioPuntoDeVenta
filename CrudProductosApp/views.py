from django.shortcuts import render

# Create your views here.
def renderTemplateCrudProductos (request):
    return render(request, "templateCrudProducto/crudproducto.html")


def renderTemplateFormularioAgregarProducto (request):
    return render(request, "templateCrudProducto/formulario-producto.html")
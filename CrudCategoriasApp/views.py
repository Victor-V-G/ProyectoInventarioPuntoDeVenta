from django.shortcuts import render

# Create your views here.
def renderTemplateCrudCategorias (request):
    return render(request, "templateCrudCategoria/crudcategoria.html")


def renderTemplateFormularioCategoria (request):
    return render(request, "templateCrudCategoria/formulario-categoria.html")
from django.shortcuts import render

# Create your views here.
def renderTemplateCrudCategorias (request):
    return render(request, "templateCrudCategoria/crudcategoria.html")
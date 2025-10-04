from django.shortcuts import render
from CrudProductosApp.models import Producto

# Create your views here.
def renderTemplateCrudProductos (request):
    return render(request, "templateCrudProducto/crudproducto.html")


def renderTemplateFormularioAgregarProducto (request):
    return render(request, "templateCrudProducto/formulario-producto.html")

#Models
def productoData(request):
    producto = Producto.objects.all()
    data = {'Producto' : producto}
    return render(request, 'templateCrudProducto/producto-models.html', data)
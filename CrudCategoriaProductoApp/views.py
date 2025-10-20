from django.shortcuts import render, redirect
from CrudCategoriaProductoApp.models import CategoriaProducto
from . import forms
from django.contrib import messages


# Create your views here.
def categoriaProductoData(request):
    
    categoriaProducto = CategoriaProducto.objects.all()
    data = {'CategoriaProducto': categoriaProducto}
    return render(request, 'templateCrudCategoriaProducto/categoriaProducto-models.html', data)

def categoriaProductoRegistracionView(request):
    form = forms.CategoriaProductoRegistracionForm()

    if request.method == 'POST':
        form = forms.CategoriaProductoRegistracionForm(request.POST)
        if form.is_valid():
            print("FORM VALIDO")
            print("NOMBRE: ", form.cleaned_data['NombreCategoria'])
            print("DESCRIPCION: ", form.cleaned_data['Descripcion'])
            print("ESTADO: ", form.cleaned_data['Estado'])
            print("OBSERVACIONES: ", form.cleaned_data['Observaciones'])

            form.save()
            messages.success(request, "Categoria registrada correctamente")
        else:
            messages.error(request, "Corrige los errores en el formulario antes de continuar")
    
    data = {
        'form': form,
        'valor': form.is_valid()}
    return render(request, 'templateCrudCategoriaProducto/registro-categoriaProducto.html', data)


def actualizarCategoriaProducto(request, IdCategoriaProducto):

    categoriaProducto = CategoriaProducto.objects.get(IdCategoriaProducto=IdCategoriaProducto)
    form = forms.CategoriaProductoRegistracionForm(instance=categoriaProducto)

    if request.method == 'POST':
        form = forms.CategoriaProductoRegistracionForm(request.POST, instance=categoriaProducto)

        if form.is_valid():
            form.save()
    
    data = {
        'form': form,
        'valor': form.is_valid()}
    return render(request, 'templateCrudCategoriaProducto/registro-categoriaProducto.html', data)


def confirmarEliminar(request, IdCategoriaProducto):
    categoriaProducto = CategoriaProducto.objects.get(IdCategoriaProducto=IdCategoriaProducto)
    data = {'bod' : categoriaProducto}
    return render(request, 'templateCrudCategoriaProducto/confirmar-eliminar.html', data)


def eliminarCategoriaProducto(request, IdCategoriaProducto):
    categoriaProducto = CategoriaProducto.objects.get(IdCategoriaProducto=IdCategoriaProducto)
    if request.method == 'POST':
        categoriaProducto.delete()
        messages.success(request, f"La categoria '{categoriaProducto.NombreCategoria}' fue eliminado correctamente.")
        return render(request, 'templateCrudCategoriaProducto/redireccion.html')
    else:
        messages.error(request, "Método no permitido para eliminar usuarios.")

#Detalle
def detalleCategoriaProducto(request, IdCategoriaProducto):
    categoriaProducto = CategoriaProducto.objects.get(IdCategoriaProducto=IdCategoriaProducto)
    data = {'bod' : categoriaProducto}
    return render(request, 'templateCrudCategoriaProducto/detalle-categoriaProducto.html', data)
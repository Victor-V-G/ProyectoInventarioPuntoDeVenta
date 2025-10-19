from django.shortcuts import render, redirect
from CrudCategoriaProductoApp.models import CategoriaProducto
from . import forms

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

def eliminarCategoriaProducto(request, IdCategoriaProducto):

    categoriaProducto = CategoriaProducto.objects.get(IdCategoriaProducto=IdCategoriaProducto)
    categoriaProducto.delete()
    return redirect('/adminhome/crud-categoriaProducto/')
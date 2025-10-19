from django.shortcuts import render, redirect
from CrudBodegasApp.models import Bodegas
from . import forms

# Create your views here.
def bodegasData(request):
    bodegas = Bodegas.objects.all()
    data = {'Bodegas': bodegas}
    return render(request, 'templateCrudBodega/bodegas-models.html', data)


def bodegasRegistracionView(request):
    form = forms.BodegaRegistracionForm()

    if request.method == 'POST':
        form = forms.BodegaRegistracionForm(request.POST)
        if form.is_valid():
            print("FORM VALIDO")
            print("NOMBRE: ", form.cleaned_data['NombreBodega'])
            print("UBICACION: ", form.cleaned_data['UbicacionBodega'])
            print("ESTADO DE LA BODEGA: ", form.cleaned_data['EstadoBodega'])
            print("OBSERVACIONES: ", form.cleaned_data['ObservacionesBodega'])
            form.save()

    data = {
        'form': form,
        'valor': form.is_valid()
        }
    return render(request, 'templateCrudBodega/registro-bodega.html', data)


def actualizarBodega(request, IdBodega):
    bodega = Bodegas.objects.get(IdBodega=IdBodega)
    form = forms.BodegaRegistracionForm(instance=bodega)

    if request.method == 'POST':
        form = forms.BodegaRegistracionForm(request.POST, instance=bodega)

        if form.is_valid():
            form.save()

    data = {
        'form': form,
        'valor': form.is_valid()
        }
    return render(request, 'templateCrudBodega/registro-bodega.html', data)


def eliminarBodega(request, IdBodega):
    bodega = Bodegas.objects.get(IdBodega=IdBodega)
    bodega.delete()
    return redirect('/adminhome/crud-bodegas/')




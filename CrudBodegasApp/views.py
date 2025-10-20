from django.shortcuts import render, redirect
from CrudBodegasApp.models import Bodegas
from . import forms
from django.contrib import messages

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
            messages.success(request, "Producto registrado correctamente")
        else:
            messages.error(request, "Corrige los errores en el formulario antes de continuar")


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
            messages.success(request, "Producto actualizado correctamente")
        else:
            messages.error(request, "Corrige los errores en el formulario antes de continuar")

    data = {
        'form': form,
        'valor': form.is_valid()
        }
    return render(request, 'templateCrudBodega/registro-bodega.html', data)

def confirmarEliminar(request, IdBodega):
    bodega = Bodegas.objects.get(IdBodega=IdBodega)
    data = {'bod' : bodega}
    return render(request, 'templateCrudBodega/confirmar-eliminar.html', data)


def eliminarBodega(request, IdBodega):
    bodega = Bodegas.objects.get(IdBodega=IdBodega)
    if request.method == 'POST':
        bodega.delete()
        messages.success(request, f"La Bodega '{bodega.NombreBodega}' fue eliminada correctamente.")
        return render(request, 'templateCrudBodega/redireccion.html')
    else:
        messages.error(request, "Método no permitido para eliminar usuarios.")


#Detalle
def detalleBodega(request, IdBodega):
    bodega = Bodegas.objects.get(IdBodega=IdBodega)
    data = {'bod' : bodega}
    return render(request, 'templateCrudBodega/detalle-bodega.html', data)
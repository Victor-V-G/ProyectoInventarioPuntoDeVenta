from django.shortcuts import render, redirect
from CrudCargosApp.models import Cargos
from . import forms

# Create your views here.
def cargosData(request):
    cargos = Cargos.objects.all()
    data = {'Cargos': cargos}
    return render(request, 'templateCrudCargo/cargos-models.html', data)


def cargosRegistracionView(request):
    form = forms.CargoRegistracionForm()

    if request.method == 'POST':
        form = forms.CargoRegistracionForm(request.POST)
        if form.is_valid():
            print("FORM VALIDO")
            print("TIPO DE CARGO: ", form.cleaned_data['TipoDeCargo'])
            print("ESTADO DEL CARGO: ", form.cleaned_data['EstadoDelCargo'])
            print("DESCRIPCION DEL CARGO: ", form.cleaned_data['DescripcionDelCargo'])
            print("SUELDO BASE: ", form.cleaned_data['SueldoBase'])

            form.save()
            return redirect('/adminhome/crud-cargos/')
    
    data = {'form': form}
    return render(request, 'templateCrudCargo/registro-cargo.html', data)


def actualizarCargo(request, IdCargos):
    cargo = Cargos.objects.get(IdCargos=IdCargos)
    form = forms.CargoRegistracionForm(instance=cargo)

    if request.method == 'POST':
        form = forms.CargoRegistracionForm(request.POST, instance=cargo)

        if form.is_valid():
            form.save()
            return redirect('/adminhome/crud-cargos/')
    
    data = {'form': form}
    return render(request, 'templateCrudCargo/registro-cargo.html', data)


def eliminarCargo(request, IdCargos):
    cargo = Cargos.objects.get(IdCargos=IdCargos)
    cargo.delete()
    return redirect('/adminhome/crud-cargos/')
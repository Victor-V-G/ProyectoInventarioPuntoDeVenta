from django.shortcuts import render, redirect
from CrudCargosApp.models import Cargos
from . import forms
from django.contrib import messages

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
            messages.success(request, "Cargo registrado correctamente")
            return redirect('/adminhome/crud-cargos/')
        else:
            messages.error(request, "Corrige los errores en el formulario antes de continuar")

    
    data = {'form': form}
    return render(request, 'templateCrudCargo/registro-cargo.html', data)


def actualizarCargo(request, IdCargos):
    cargo = Cargos.objects.get(IdCargos=IdCargos)
    form = forms.CargoRegistracionForm(instance=cargo)

    if request.method == 'POST':
        form = forms.CargoRegistracionForm(request.POST, instance=cargo)

        if form.is_valid():
            form.save()
            messages.success(request, "Cargo actualizado correctamente")
            return redirect('/adminhome/crud-cargos/')
        else:
            messages.error(request, "Corrige los errores en el formulario antes de continuar")
    
    data = {'form': form}
    return render(request, 'templateCrudCargo/registro-cargo.html', data)

#Eliminar
def confirmarEliminar(request, IdCargos):
    cargo = Cargos.objects.get(IdCargos=IdCargos)
    data = {'cag' : cargo}
    return render(request, 'templateCrudCargo/confirmar-eliminar.html', data)


def eliminarCargo(request, IdCargos):
    cargo = Cargos.objects.get(IdCargos=IdCargos)

    if request.method == 'POST':
        cargo.delete()
        messages.success(request, f"El cargo '{cargo.TipoDeCargo}' fue eliminado correctamente.")
        return redirect('/adminhome/crud-cargos/')
    else:
        messages.error(request, "Método no permitido para eliminar usuarios.")
        return redirect('/adminhome/crud-cargos/')
    

#Detalle
def detalleCargo(request, IdCargos):
    cargo = Cargos.objects.get(IdCargos=IdCargos)
    data = {'cag' : cargo}
    return render(request, 'templateCrudCargo/detalle-cargo.html', data)


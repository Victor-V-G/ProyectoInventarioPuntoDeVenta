from django.shortcuts import render, redirect
from CrudUsuariosApp.models import Usuarios
from . import forms
from django.contrib import messages

#Models
def usuariosData(request):
    usuarios = Usuarios.objects.all()
    data = {'Usuarios' : usuarios}
    return render(request, 'templateCrudUsuario/usuarios-models.html', data)


#Form
def usuariosRegistrationView(request):
    form = forms.UsuarioRegistrationForm()

    if request.method == 'POST':
        form = forms.UsuarioRegistrationForm(request.POST)
        if form.is_valid():
            print("FORM ES VALIDO")
            print("USERNAME: ", form.cleaned_data['Username'])
            print("PASSWORD: ", form.cleaned_data['Password'])
            print("CONFIRMAR PASSWORD: ", form.cleaned_data['ConfirmarPassword'])
            print("CORREO ELECTRONICO: ", form.cleaned_data['CorreoElectronico'])
            
            form.save()
            messages.success(request, "Usuario registrado correctamente")
            return redirect('/adminhome/crud-usuarios')
        else:
            messages.error(request, "Corrige los errores en el formulario antes de continuar")
        
    data = {'form': form}
    return render(request, 'templateCrudUsuario/registro-usuario.html', data)


#Actualizar
def actualizarUsuario(request, IdUsuarios):
    usuario = Usuarios.objects.get(IdUsuarios=IdUsuarios)
    form = forms.UsuarioRegistrationForm(instance=usuario)

    if request.method == 'POST':
        form = forms.UsuarioRegistrationForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('/adminhome/crud-usuarios/')
        
    data = {'form': form}
    return render(request, 'templateCrudUsuario/registro-usuario.html', data)


#Eliminar
def confirmarEliminar(request, IdUsuarios):
    usuario = Usuarios.objects.get(IdUsuarios=IdUsuarios)
    data = {'usu' : usuario}
    return render(request, 'templateCrudUsuario/confirmar-eliminar.html', data)


def eliminarUsuario(request, IdUsuarios):
    usuario = Usuarios.objects.get(IdUsuarios=IdUsuarios)
    usuario.delete()
    return redirect('/adminhome/crud-usuarios/')


#Detalle
def detalleUsuario(request, IdUsuarios):
    usuario = Usuarios.objects.get(IdUsuarios=IdUsuarios)
    data = {'usu' : usuario}
    return render(request, 'templateCrudUsuario/detalle-usuario.html', data)


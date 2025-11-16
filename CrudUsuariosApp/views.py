from django.shortcuts import render, redirect
from CrudUsuariosApp.models import Usuarios
from . import forms
from django.contrib import messages
from AuditoriaApp.views import RegistrarAuditoriaUsuario
from LoginApp.decorators import solo_admin

#Models
@solo_admin
def usuariosData(request):
    usuarios = Usuarios.objects.all()
    data = {'Usuarios' : usuarios}
    return render(request, 'templateCrudUsuario/usuarios-models.html', data)


#Form
@solo_admin
def usuariosRegistrationView(request):
    form = forms.UsuarioRegistrationForm()
    actualizar = False

    if request.method == 'POST':
        form = forms.UsuarioRegistrationForm(request.POST)
        if form.is_valid():
            print("FORM ES VALIDO")
            print("USERNAME: ", form.cleaned_data['Username'])
            print("PASSWORD: ", form.cleaned_data['Password'])
            print("CONFIRMAR PASSWORD: ", form.cleaned_data['ConfirmarPassword'])
            print("CORREO ELECTRONICO: ", form.cleaned_data['CorreoElectronico'])
            print("EMPLEADO SELECCIONADO", form.cleaned_data['Empleado'])
            print("CARGO SELECCIONADO", form.cleaned_data['Cargo'])
            
            usuario_registrado = form.save()
            RegistrarAuditoriaUsuario(request, usuario_registrado, "REGISTRAR")
            messages.success(request, "Usuario registrado correctamente")
            return redirect('admin-crud-usuario')
        else:
            messages.error(request, "Corrige los errores en el formulario antes de continuar")
        
    data = {
        'form': form,
        'actualizar': actualizar
    }
    return render(request, 'templateCrudUsuario/registro-usuario.html', data)


#Actualizar
@solo_admin
def actualizarUsuario(request, IdUsuarios):
    usuario = Usuarios.objects.get(IdUsuarios=IdUsuarios)
    form = forms.UsuarioUpdateForm(instance=usuario)
    actualizar = True

    if request.method == 'POST':
        form = forms.UsuarioUpdateForm(request.POST, instance=usuario)
        if form.is_valid():
            usuario_actualizado = form.save()
            RegistrarAuditoriaUsuario(request, usuario_actualizado, "ACTUALIZAR")
            messages.success(request, "Usuario actualizado correctamente")
            return redirect('admin-crud-usuario')
        else:
            messages.error(request, "Corrige los errores en el formulario antes de continuar")
            
    data = {
        'form': form,
        'actualizar': actualizar,
        'UsuarioActual': usuario
    }
    return render(request, 'templateCrudUsuario/registro-usuario.html', data)


#Eliminar
@solo_admin
def confirmarEliminar(request, IdUsuarios):
    usuario = Usuarios.objects.get(IdUsuarios=IdUsuarios)
    data = {'usu' : usuario}
    return render(request, 'templateCrudUsuario/confirmar-eliminar.html', data)

@solo_admin
def eliminarUsuario(request, IdUsuarios):
    usuario = Usuarios.objects.get(IdUsuarios=IdUsuarios)

    if request.method == 'POST':
        RegistrarAuditoriaUsuario(request, usuario, "ELIMINAR")
        usuario.delete()
        messages.success(request, f"El usuario '{usuario.Username}' fue eliminado correctamente.")
        return redirect('admin-crud-usuario')
    else:
        messages.error(request, "Método no permitido para eliminar usuarios.")
        return redirect('admin-crud-usuario')


#Detalle
@solo_admin
def detalleUsuario(request, IdUsuarios):
    usuario = Usuarios.objects.get(IdUsuarios=IdUsuarios)
    data = {'usu' : usuario}
    return render(request, 'templateCrudUsuario/detalle-usuario.html', data)


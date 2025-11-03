from django.shortcuts import render, redirect
from . import forms
from CrudUsuariosApp.models import Usuarios
from django.contrib import messages
from django.contrib.auth.hashers import check_password
# Create your views here.


#ESTA VIEW PERMITE RENDERIZAR EL TEMPLATES DE LOGIN
def renderlogin(request):
    # Renderiza y devuelve el template de login al navegador
    return render(request, 'templateLogin/login.html')


def renderLoginForm(request):
    form = forms.LoginForm(request.POST)
    data = {'form': form}

    if request.method == 'POST':
        UsernameInput = request.POST['UsernameField']
        PasswordInput = request.POST['PasswordField']

        try:
            UsuarioRecuperado = Usuarios.objects.get(Username=UsernameInput)
        except Usuarios.DoesNotExist:
            messages.error(request, "El username ingresado no existe")
            return render(request, 'templateLogin/login-form.html', data)

        if check_password(PasswordInput, UsuarioRecuperado.Password):
            print("Loggeo Correcto")

            request.session['Usuario_Username'] = UsuarioRecuperado.Username

            UsuarioLogeado = request.session.get('Usuario_Username')
            print(UsuarioLogeado)

            if UsuarioLogeado == "Admin":
                return redirect('adminhome/')
            else:
                return redirect('home/')
            
        else:
            messages.error(request, "Password incorrecta, intentelo nuevamente.")

    return render(request, 'templateLogin/login-form.html', data)
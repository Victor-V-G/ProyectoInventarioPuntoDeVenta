from django.shortcuts import redirect


def login_requerido(funcion_envuelta):
    def funcion_reemplazada(request, *args, **kwargs):
        print("DEBUG -> Usuario_Username:", request.session.get("Usuario_Username"))
        if not request.session.get("Usuario_Username"):
            return redirect('Login')
        return funcion_envuelta(request, *args, **kwargs)
    return funcion_reemplazada


def solo_admin(funcion_envuelta):
    def funcion_reemplazada(request, *args, **kwargs):
        UsuarioLogeado = request.session.get("Usuario_Username")
        if UsuarioLogeado != "Admin":
            return redirect('home')
        return funcion_envuelta(request, *args, **kwargs)
    return funcion_reemplazada
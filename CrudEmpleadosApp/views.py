# Importaciones necesarias
from django.shortcuts import render, redirect  # 'render' para mostrar templates y 'redirect' para redirigir a otra URL
from CrudEmpleadosApp.models import Empleados  # Importa el modelo Empleados desde la app CrudEmpleadosApp
from . import forms  # Importa los formularios definidos en forms.py de la misma app
from django.contrib import messages
# Nota general:
# Se utiliza 'redirect' después de procesar un formulario para evitar problemas de rutas
# y evitar que se vuelvan a enviar los datos si el usuario recarga la página.

# ========================================================================
# VISTA: Mostrar todos los empleados
# ========================================================================
def empleadosData(request):
    """
    Obtiene todos los registros de empleados de la base de datos
    y los envía al template 'empleados-models.html' para mostrarlos.

    Parámetros:
    - request: Objeto HttpRequest que contiene información sobre la solicitud HTTP.

    Retorna:
    - render: Renderiza el template con los datos de los empleados.
    """
    empleados = Empleados.objects.all()  # Consulta todos los registros de la tabla Empleados
    data = {'Empleados': empleados}  # Diccionario que se pasará al template
    return render(request, 'templateCrudEmpleado/empleados-models.html', data)


# ========================================================================
# VISTA: Registro de un nuevo empleado
# ========================================================================
def empleadoRegistrationView(request):
    """
    Permite registrar un nuevo empleado mediante un formulario.
    Si la solicitud es POST y el formulario es válido, guarda los datos
    y redirige a la página de listado de empleados.

    Parámetros:
    - request: Objeto HttpRequest que contiene información sobre la solicitud HTTP.

    Retorna:
    - render: Renderiza el template 'registro-empleado.html' con el formulario.
    """
    form = forms.EmpleadoRegistrationForm()  # Inicializa un formulario vacío

    if request.method == 'POST':  # Verifica si se envió el formulario
        form = forms.EmpleadoRegistrationForm(request.POST)  # Crea un formulario con los datos enviados
        if form.is_valid():  # Valida los datos del formulario
            # Se imprimen los datos validados en consola para depuración
            print("FORM ES VALIDO")
            print("RUT: ", form.cleaned_data['RutEmpleado'])
            print("NOMBRE: ", form.cleaned_data['NombreEmpleado'])
            print("APELLIDO: ", form.cleaned_data['ApellidoEmpleado'])
            print("EDAD: ", form.cleaned_data['EdadEmpleado'])
            print("TELEFONO: ", form.cleaned_data['NumeroTelefonoEmpleado'])
            
            form.save()  # Guarda el nuevo empleado en la base de datos
            messages.success(request, "Empleado registrado correctamente")
            return redirect('/adminhome/crud-empleado/')  # Redirige a la página de listado de empleados
        else:
            messages.error(request, "Corrige los errores en el formulario antes de continuar")
            
    data = {'form': form}  # Diccionario con el formulario para enviarlo al template
    return render(request, 'templateCrudEmpleado/registro-empleado.html', data)


# ========================================================================
# VISTA: Actualizar un empleado existente
# ========================================================================
def actualizarEmpleado(request, IdEmpleado):
    """
    Permite actualizar los datos de un empleado existente.
    El campo RUT se deshabilita para que no pueda ser modificado,
    ya que es la clave primaria.

    Parámetros:
    - request: Objeto HttpRequest con información de la solicitud.
    - Rut: Identificador único del empleado a actualizar.

    Retorna:
    - render: Renderiza el template 'registro-empleado.html' con el formulario.
    """
    empleado = Empleados.objects.get(IdEmpleado=IdEmpleado)  # Obtiene el empleado por su RUT
    form = forms.EmpleadoRegistrationForm(instance=empleado)  # Crea un formulario precargado con los datos del empleado

    if request.method == 'POST':  # Si se envían datos para actualizar
        form = forms.EmpleadoRegistrationForm(request.POST, instance=empleado)  # Vincula los datos al formulario
        if form.is_valid():  # Valida el formulario
            form.save()  # Guarda los cambios en la base de datos
            return redirect('/adminhome/crud-empleado/')  # Redirige al listado de empleados

    data = {'form': form}  # Diccionario con el formulario
    return render(request, 'templateCrudEmpleado/registro-empleado.html', data)


# ========================================================================
# VISTA: Eliminar un empleado
# ========================================================================
def confirmarEliminar(request, IdEmpleado):
    empleado = Empleados.objects.get(IdEmpleado=IdEmpleado)
    data = {'emp' : empleado}
    return render(request, 'templateCrudEmpleado/confirmar-eliminar.html', data)


def eliminarEmpleado(request, IdEmpleado):
    empleado = Empleados.objects.get(IdEmpleado=IdEmpleado)  # Obtiene el empleado a eliminar
    if request.method == 'POST':
        empleado.delete()
        messages.success(request, f"El empleado '{empleado.NombreEmpleado}' fue eliminado correctamente.")
        return redirect('/adminhome/crud-empleado/')
    else:
        messages.error(request, "Método no permitido para eliminar usuarios.")
        return redirect('/adminhome/crud-empleado/')
    
#Detalle
def detalleEmpleado(request, IdEmpleado):
    empleado = Empleados.objects.get(IdEmpleado=IdEmpleado) 
    data = {'emp' : empleado}
    return render(request, 'templateCrudEmpleado/detalle-empleado.html', data)

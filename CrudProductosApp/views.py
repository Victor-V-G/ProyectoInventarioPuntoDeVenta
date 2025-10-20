# Importaciones necesarias
from django.shortcuts import render, redirect  # 'render' para mostrar templates y 'redirect' para redirigir
from CrudProductosApp.models import Productos  # Importa el modelo Producto
from . import forms  # Importa los formularios de la app CrudProductosApp
from django.contrib import messages

# ========================================================================
# VISTA: Mostrar todos los productos
# ========================================================================
def productosData(request):
    """
    Obtiene todos los registros de productos de la base de datos
    y los envía al template 'producto-models.html' para mostrarlos.

    Parámetros:
    - request: Objeto HttpRequest que contiene información sobre la solicitud HTTP.

    Retorna:
    - render: Renderiza el template con los datos de los productos.
    """
    productos = Productos.objects.all()  # Consulta todos los productos
    data = {'Productos': productos}  # Diccionario con los datos para el template
    return render(request, 'templateCrudProducto/productos-models.html', data)


# ========================================================================
# VISTA: Registro de un nuevo producto
# ========================================================================
def productosRegistrationView(request):
    """
    Permite registrar un nuevo producto mediante un formulario.
    Si la solicitud es POST y el formulario es válido, guarda los datos
    y redirige a la página de listado de productos.

    Parámetros:
    - request: Objeto HttpRequest que contiene información sobre la solicitud HTTP.

    Retorna:
    - render: Renderiza el template 'registro-producto.html' con el formulario.
    """
    form = forms.ProductoRegistrationForm()  # Inicializa un formulario vacío

    if request.method == 'POST':  # Verifica si se envió el formulario
        form = forms.ProductoRegistrationForm(request.POST)  # Crea un formulario con los datos enviados
        if form.is_valid():  # Valida los datos del formulario
            # Imprime en consola los datos validados para depuración
            print("FORM ES VALIDO")
            print("CODIGO DE BARRAS: ", form.cleaned_data['CodigoDeBarras'])
            print("VALOR: ", form.cleaned_data['ValorProducto'])
            print("STOCK: ", form.cleaned_data['StockProducto'])
            print("NOMBRE DEL PRODUCTO: ", form.cleaned_data['NombreProducto'])
            print("MARCA: ", form.cleaned_data['MarcaProducto'])
            print("FECHA DE VENCIMIENTO: ", form.cleaned_data['FechaDeVencimiento'])
            
            form.save()  # Guarda el nuevo producto en la base de datos
            messages.success(request, "Producto registrado correctamente")
        else:
            messages.error(request, "Corrige los errores en el formulario antes de continuar")
    
    data = {
        'form': form,
        'valor': form.is_valid()}  # Diccionario con el formulario
    return render(request, 'templateCrudProducto/registro-producto.html', data)


# ========================================================================
# VISTA: Actualizar un producto existente
# ========================================================================
def actualizarProducto(request, IdProducto):
    """
    Permite actualizar los datos de un producto existente.

    Parámetros:
    - request: Objeto HttpRequest con información de la solicitud.
    - IdProducto: Identificador único del producto a actualizar.

    Retorna:
    - render: Renderiza el template 'registro-producto.html' con el formulario.
    """
    producto = Productos.objects.get(IdProducto=IdProducto)  # Obtiene el producto por su ID
    form = forms.ProductoRegistrationForm(instance=producto)  # Formulario precargado con datos del producto

    if request.method == 'POST':  # Si se envían datos para actualizar
        form = forms.ProductoRegistrationForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()  # Guarda los cambios en la base de datos
            messages.success(request, "Producto Actualizado correctamente")
        else:
            messages.error(request, "Corrige los errores en el formulario antes de continuar")
            
    data = {
        'form': form,
        'valor': form.is_valid()}  # Diccionario con el formulario
    return render(request, 'templateCrudProducto/registro-producto.html', data)


# ========================================================================
# VISTA: Eliminar un producto
# ========================================================================


def confirmarEliminar(request, IdProducto):
    producto = Productos.objects.get(IdProducto=IdProducto)
    data = {'pro' : producto}
    return render(request, 'templateCrudProducto/confirmar-eliminar.html', data)


def eliminarProducto(request, IdProducto):
    producto = Productos.objects.get(IdProducto=IdProducto)
    if request.method == 'POST':
        producto.delete()
        messages.success(request, f"El producto '{producto.NombreProducto}' fue eliminado correctamente.")
        return render(request, 'templateCrudProducto/redireccion.html')
    else:
        messages.error(request, "Método no permitido para eliminar usuarios.")

#Detalle
def detalleProducto(request, IdProducto):
    producto = Productos.objects.get(IdProducto=IdProducto)
    data = {'pro' : producto}
    return render(request, 'templateCrudProducto/detalle-producto.html', data)
# Importaciones necesarias
from django.shortcuts import render, redirect  # 'render' para mostrar templates y 'redirect' para redirigir
from CrudProductosApp.models import Productos  # Importa el modelo Producto
from . import forms  # Importa los formularios de la app CrudProductosApp

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
    
    data = {
        'form': form,
        'valor': form.is_valid()}  # Diccionario con el formulario
    return render(request, 'templateCrudProducto/registro-producto.html', data)


# ========================================================================
# VISTA: Eliminar un producto
# ========================================================================
def eliminarProducto(request, IdProducto):
    """
    Elimina un producto específico de la base de datos según su IdProducto
    y redirige al listado de productos.

    Parámetros:
    - request: Objeto HttpRequest con información de la solicitud.
    - IdProducto: Identificador único del producto a eliminar.

    Retorna:
    - redirect: Redirige a la página de listado de productos después de eliminar.
    """
    producto = Productos.objects.get(IdProducto=IdProducto)  # Obtiene el producto a eliminar
    producto.delete()  # Elimina el registro de la base de datos
    return redirect('/adminhome/crud-productos/')  # Redirige al listado de productos

# Importaciones necesarias
from django import forms  # Importa el módulo de formularios de Django
from CrudProductosApp.models import Producto  # Importa el modelo Producto

# ========================================================================
# Formulario: Registro de Productos
# ========================================================================
# Este formulario permite crear o actualizar registros de productos
# usando el modelo Producto. Al heredar de ModelForm, genera automáticamente
# campos basados en el modelo.
# ========================================================================

class ProductoRegistrationForm(forms.ModelForm):
    """
    Formulario para registrar o actualizar productos.
    Hereda de forms.ModelForm, lo que permite mapear los campos del modelo automáticamente.
    """
    class Meta:
        model = Producto  # Modelo en el que se basa el formulario
        fields = '__all__'  # Incluye todos los campos del modelo en el formulario

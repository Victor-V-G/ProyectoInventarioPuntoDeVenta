# Importaciones necesarias
from django import forms  # Importa el módulo de formularios de Django
from CrudEmpleadosApp.models import Empleados  # Importa el modelo Empleados
import re

# ========================================================================
# Formulario: Registro de Empleados
# ========================================================================
# Este formulario permite crear o actualizar registros de empleados
# usando el modelo Empleados. Se basa en ModelForm, por lo que
# automáticamente genera campos según el modelo.
# ========================================================================

class EmpleadoRegistrationForm(forms.ModelForm):
    """
    Formulario para registrar o actualizar empleados.
    Hereda de forms.ModelForm, lo que permite mapear los campos del modelo automáticamente.
    """
    class Meta:
        model = Empleados  # Modelo en el que se basa el formulario
        fields = '__all__'  # Incluye todos los campos del modelo en el formulario

    # ====================================================================
    # Validaciones personalizadas
    # ====================================================================
    def clean_Rut(self):
        """
        Valida que el RUT tenga el formato chileno correcto:
        - Solo se permiten entre 7 y 8 dígitos seguidos de un guion y un dígito o 'K'.
        - Ejemplos válidos: 12345678-5, 1234567-K, 1234567-k

        Retorna:
        - inputRut: El RUT validado si cumple el formato.

        Lanza:
        - forms.ValidationError si el formato no es válido.
        """
        inputRut = self.cleaned_data.get('Rut')

        # Expresión regular para formato RUT chileno
        rut_pattern = r'^[0-9]{7,8}-[0-9Kk]$'

        # Validar formato con regex
        if not re.match(rut_pattern, inputRut):
            raise forms.ValidationError("El formato del RUT no es válido. Debe ser 00000000-0 o 00000000-K.")
        return inputRut

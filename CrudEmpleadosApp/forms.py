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

        inputRut = self.cleaned_data['Rut'].strip().upper()  # Obtiene valor y elimina espacios al inicio y fin
        caracteres = r"^\d{7,8}-[\dK]$"

        """
        Valida que el RUT tenga el formato chileno correcto:
        - Solo se permiten entre 7 y 8 dígitos seguidos de un guion y un dígito o 'K'.
        - Ejemplos válidos: 12345678-5, 1234567-K, 1234567-k

        Retorna:
        - inputRut: El RUT validado si cumple el formato.

        Lanza:
        - forms.ValidationError si el formato no es válido.
        """
        if not re.match(caracteres, inputRut):  # Valida la longitud máxima
            raise forms.ValidationError("Ingrese un Rut Valido con guion y sin puntos.")  # Mensaje de error
        if Empleados.objects.filter(Rut=inputRut).exists():
            raise forms.ValidationError("Este RUT ya está registrado.")
        return inputRut  # Devuelve el valor limpio si es válido
    
    def clean_NombreEmpleado(self):
        inputNombre = self.cleaned_data['NombreEmpleado'].strip()  # Obtiene valor y elimina espacios al inicio y fin
        caracteres = r"^[a-zA-ZñÑ]{4,}$"

        if not re.match(caracteres, inputNombre):  # Valida la longitud máxima
            raise forms.ValidationError("Ingrese un Nombre valido con solo letras y mas de 3 letras.")  # Mensaje de error
        return inputNombre  # Devuelve el valor limpio si es válido
    
    def clean_ApellidoEmpleado(self):
        inputApellido = self.cleaned_data['ApellidoEmpleado'].strip()  # Obtiene valor y elimina espacios al inicio y fin
        caracteres = r"^([a-zA-ZñÑ]{2,})( [a-zA-ZñÑ]{2,})*$"

        if not re.match(caracteres, inputApellido):  # Valida la longitud máxima
            raise forms.ValidationError("Ingrese un Apellido valido con solo letras y mas de 3 letras.")  # Mensaje de error
        return inputApellido  # Devuelve el valor limpio si es válido

    def clean_EdadEmpleado(self):
        inputedad = self.cleaned_data['EdadEmpleado']

        if inputedad < 0:
            raise forms.ValidationError("No ingrese numeros negativos.")
        if inputedad < 18:
            raise forms.ValidationError("La edad debe ser mayor o igual a 18 años.")
        if inputedad > 100:
            raise forms.ValidationError("La edad no puede ser mayor a 100 años.")
        return inputedad
    
    def clean_NumeroTelefonoEmpleado(self):
        inputtelefono = str(self.cleaned_data['NumeroTelefonoEmpleado']).strip()  # Convierte a texto por si es IntegerField
        caracteres = r"^9\d{8}$"

        if not re.match(caracteres, inputtelefono):  # Valida la longitud máxima
            raise forms.ValidationError("Ingrese un numero de solo 9 digitos, anteponiendo el nueve.")  # Mensaje de error
        return inputtelefono  # Devuelve el valor limpio si es válido

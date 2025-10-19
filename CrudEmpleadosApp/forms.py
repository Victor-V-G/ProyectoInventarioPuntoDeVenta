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

        labels = {
            'RutEmpleado': 'Rut del empleado',
            'NombreEmpleado': 'Nombre',
            'ApellidoEmpleado': 'Apellido',
            'EdadEmpleado': 'Edad',
            'NumeroTelefonoEmpleado': 'Numero telefonico',
        }
        help_texts = {
            'RutEmpleado': 'Indique el rut del empleado a registrar',
            'NombreEmpleado': 'Indique el nombre del empleado',
            'ApellidoEmpleado': 'Indique el apellido del empleado',
            'EdadEmpleado': 'Ingrese la edad del empleado',
            'NumeroTelefonoEmpleado': 'Ingrese el numero telefonico del empleado',
        }
        error_messages = {
            'RutEmpleado': {
                'required': 'Por favor introduzca el rut',
                'unique': 'Este rut ya esta registrado',
                'invalid': 'Ingrese un rut valido (01234567-k) con guion y sin puntos.',
            },
            'NombreEmpleado': {
                'required': 'Por favor introduzca el nombre del empleado',
            },
            'ApellidoEmpleado': {
                'required': 'Por favor introduzca el apellido del empleado',
            },
            'EdadEmpleado': {
                'required': 'Por favor introduzca la edad del empleado',
                'invalid': 'Ingrese una edad valida',
            },
            'NumeroTelefonoEmpleado': {
                'required': 'Por favor introduzca un numero telefonico',
                'invalid': 'Ingrese un numero telefonico valido (912345678)',
            },
        }
        widgets = {
            'RutEmpleado': forms.TextInput(attrs={
                'placeholder': 'Ej: (01234567-k)'
            }),
            'NombreEmpleado': forms.TextInput(attrs={
                'placeholder': 'Ej: Pablo'
            }),
            'ApellidoEmpleado': forms.TextInput(attrs={
                'placeholder': 'Ej: Campusano Sotomayor'
            }),
            'EdadEmpleado': forms.NumberInput(attrs={
                'placeholder': 'Ej: 20 (años)'
            }),
            'NumeroTelefonoEmpleado': forms.NumberInput(attrs={
                'placeholder': 'Ej: (912345678)'
            }),
        }







    # ====================================================================
    # Validaciones personalizadas
    # ====================================================================
    def clean_RutEmpleado(self):
        inputRut = self.cleaned_data['RutEmpleado'].strip().upper()  # Obtiene valor y elimina espacios al inicio y fin
        caracteres = r"^\d{7,8}-[\dK]$"
        query = Empleados.objects.filter(RutEmpleado=inputRut)
        """
        Valida que el RUT del empleado no exceda los 9 caracteres.
        Este método se llama automáticamente durante la validación del formulario.

        Retorna:
        - inputRut: El RUT validado si cumple la condición.

        Lanza:
        - forms.ValidationError si el RUT excede los 9 caracteres.
        """
        if not re.match(caracteres, inputRut):  # Valida la longitud máxima
            raise forms.ValidationError("Ingrese un Rut Valido con guion y sin puntos.")  # Mensaje de error
        if self.instance.pk:
            query = query.exclude(pk=self.instance.pk)
        if query.exists():
            raise forms.ValidationError("Este RUT ya está registrado.")
        return inputRut  # Devuelve el valor limpio si es válido
    
    def clean_NombreEmpleado(self):
        inputNombre = self.cleaned_data['NombreEmpleado'].strip().capitalize()  # Obtiene valor y elimina espacios al inicio y fin
        caracteres = r"^[A-ZÁÉÍÓÚÑa-záéíóúñ]{3,}$"

        if not re.match(caracteres, inputNombre):  # Valida la longitud máxima
            raise forms.ValidationError("Ingrese un Nombre valido con solo letras y sin espacios.")  # Mensaje de error
        return inputNombre  # Devuelve el valor limpio si es válido
    
    def clean_ApellidoEmpleado(self):
        inputApellido = self.cleaned_data['ApellidoEmpleado'].strip().title()  # Obtiene valor y elimina espacios al inicio y fin
        caracteres = r"^([A-ZÁÉÍÓÚÑa-záéíóúñ]{2,})( [A-ZÁÉÍÓÚÑa-záéíóúñ]{2,})*$"

        if not re.match(caracteres, inputApellido):  # Valida la longitud máxima
            raise forms.ValidationError("Ingrese un Apellido valido con solo letras.")  # Mensaje de error
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
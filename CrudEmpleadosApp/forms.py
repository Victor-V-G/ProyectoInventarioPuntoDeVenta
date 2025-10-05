# Importaciones necesarias
from django import forms  # Importa el módulo de formularios de Django
from CrudEmpleadosApp.models import Empleados  # Importa el modelo Empleados

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
    def clean_RutEmpleado(self):
        """
        Valida que el RUT del empleado no exceda los 9 caracteres.
        Este método se llama automáticamente durante la validación del formulario.

        Retorna:
        - inputRut: El RUT validado si cumple la condición.

        Lanza:
        - forms.ValidationError si el RUT excede los 9 caracteres.
        """
        inputRut = self.cleaned_data['Rut']  # Obtiene el valor ingresado en el formulario
        if len(inputRut) > 9:  # Valida la longitud máxima
            raise forms.ValidationError("El largo máximo del RUT son 9 caracteres.")  # Mensaje de error
        return inputRut  # Devuelve el valor limpio si es válido

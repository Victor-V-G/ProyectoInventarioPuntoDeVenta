from django import forms
from CrudCargosApp.models import Cargos

class CargoRegistracionForm(forms.ModelForm):

    class Meta:
        model = Cargos
        fields = '__all__'
        labels = {
            'TipoDeCargo': 'Tipo de cargo',
            'EstadoDelCargo': 'Estado del cargo',
        }
        help_texts = {
            'TipoDeCargo': 'Seleccione el tipo de cargo',
            'EstadoDelCargo': 'Ingrese el estado del cargo a registrar',
        }
        error_messages = {
            'TipoDeCargo': {
                'required': 'Por favor seleccione un tipo de cargo disponibles',
            },
            'EstadoDelCargo': {
                'required': 'Por favor ingrese un estado del cargo a registrar',
            },
        }
        widgets = {
            'TipoDeCargo': forms.Select(attrs={
                'placeholder': 'Ej: Bodeguero'
            }),
            'EstadoDelCargo': forms.TextInput(attrs={
                'placeholder': 'Ej: Activo o Inactivo'
            }),
        }


    def clean_NombreEmpleado(self):
        inputNombre = self.cleaned_data['TipoDeCargo']
        if len(inputNombre) > 5:
            raise forms.ValidationError("El largo del nombre debe ser mas de 5 caracteres")
        return inputNombre
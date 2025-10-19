from django import forms
from CrudCargosApp.models import Cargos

class CargoRegistracionForm(forms.ModelForm):

    class Meta:
        model = Cargos
        fields = '__all__'
        labels = {
            'TipoDeCargo': 'Tipo de cargo',
            'EstadoDelCargo': 'Estado del cargo',
            'DescripcionDelCargo': 'Descripción del cargo',
            'SueldoBase': 'Sueldo base'
        }
        help_texts = {
            'TipoDeCargo': 'Seleccione el tipo de cargo',
            'EstadoDelCargo': 'Ingrese el estado del cargo a registrar',
            'DescripcionDelCargo': 'Ingrese una breve descripción de las funciones y responsabilidades del cargo',
            'SueldoBase': 'Ingrese el sueldo base correspondiente al cargo. Mínimo permitido: $150.000'
        }
        error_messages = {
            'TipoDeCargo': {
                'required': 'Por favor seleccione un tipo de cargo disponibles',
            },
            'EstadoDelCargo': {
                'required': 'Por favor ingrese un estado del cargo a registrar',
            },
            'DescripcionDelCargo': {
                'required': 'Por favor ingrese una descripción del cargo.',
                'min_length': 'La descripción debe tener al menos 10 caracteres.'
            },
            'SueldoBase': {
                'required': 'Debe ingresar el sueldo base correspondiente.',
                'min_value': 'El sueldo base no puede ser menor a $150.000.'
            }
        }
        widgets = {
            'TipoDeCargo': forms.Select(attrs={
                'placeholder': 'Ej: Bodeguero'
            }),
            'EstadoDelCargo': forms.Select(attrs={
                'placeholder': 'Ej: Activo o Inactivo'
            }),
            'DescripcionDelCargo': forms.Textarea(attrs={
                'placeholder': 'Ej: Responsable de supervisar el orden, registro y entrega de productos dentro de la bodega.'
            }),
            'SueldoBase': forms.NumberInput(attrs={
                'placeholder': 'Ej: 450000'
            })
        }


    def clean_NombreEmpleado(self):
        inputNombre = self.cleaned_data['TipoDeCargo']
        if len(inputNombre) > 5:
            raise forms.ValidationError("El largo del nombre debe ser mas de 5 caracteres")
        return inputNombre
    

    def clean_DescripcionDelCargo(self):
        inputDescripcionDelCargo = self.cleaned_data['DescripcionDelCargo'].strip()
        if len(inputDescripcionDelCargo) < 10:
            raise forms.ValidationError("La descripción del cargo debe tener al menos 10 caracteres")
        return inputDescripcionDelCargo
    

    def clean_DescripcionDelCargo(self):
        inputDescripcionDelCargo = self.cleaned_data['DescripcionDelCargo'].strip()
        if inputDescripcionDelCargo.isdigit():
            raise forms.ValidationError("La descripción no puede contener solo números")
        return inputDescripcionDelCargo


    def clean_SueldoBase(self):
        inputSueldoBase = self.cleaned_data['SueldoBase']
        if inputSueldoBase <= 0:
            raise forms.ValidationError("El sueldo base debe ser mayor a 0")
        return inputSueldoBase

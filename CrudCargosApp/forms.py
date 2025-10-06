from django import forms
from CrudCargosApp.models import Cargos

class CargoRegistracionForm(forms.ModelForm):

    class Meta:
        model = Cargos
        fields = '__all__'

    def clean_NombreEmpleado(self):
        inputNombre = self.cleaned_data['TipoDeCargo']
        if len(inputNombre) > 5:
            raise forms.ValidationError("El largo del nombre debe ser mas de 5 caracteres")
        return inputNombre
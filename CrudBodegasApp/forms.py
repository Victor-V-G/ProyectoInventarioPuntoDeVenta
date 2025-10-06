from django import forms
from CrudBodegasApp.models import Bodegas

class BodegaRegistracionForm(forms.ModelForm):

    class Meta:
        model = Bodegas
        fields = '__all__'

    def clean_NombreEmpleado(self):
        inputNombre = self.cleaned_data['NombreBodega']
        if len(inputNombre) > 5:
            raise forms.ValidationError("El largo del nombre debe ser mas de 5 caracteres")
        return inputNombre
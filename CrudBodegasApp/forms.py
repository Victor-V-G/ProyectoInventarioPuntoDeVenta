from django import forms
from CrudBodegasApp.models import Bodegas
import re

class BodegaRegistracionForm(forms.ModelForm):

    class Meta:
        model = Bodegas
        fields = '__all__'

    def clean_NombreBodega(self):
        inputNombreBodega = self.cleaned_data['NombreBodega'].strip().upper()  # Obtiene valor y elimina espacios al inicio y fin
        caracteres = r"^([a-zA-ZñÑ]{2,}[0-9]*|\d+)( ([a-zA-ZñÑ]{2,}[0-9]*|\d+))*$"

        if not re.match(caracteres, inputNombreBodega):  # Valida la longitud máxima
            raise forms.ValidationError("Ingrese un nombre de bodega sin caracteres especiales y de mas de 5 letras.")  # Mensaje de error
        if Bodegas.objects.filter(NombreBodega=inputNombreBodega).exists():
            raise forms.ValidationError("Este Nombre de Bodega ya está registrado.")
        return inputNombreBodega  # Devuelve el valor limpio si es válido}
    
    def clean_UbicacionBodega(self):
        inputUbicacionBodega = self.cleaned_data['UbicacionBodega'].strip().upper()  # Obtiene valor y elimina espacios al inicio y fin
        caracteres = r"^([a-zA-ZñÑ]{2,}[0-9]*|\d+)( ([a-zA-ZñÑ]{2,}[0-9]*|\d+))*$"

        if not re.match(caracteres, inputUbicacionBodega):  # Valida la longitud máxima
            raise forms.ValidationError("Ingrese la ubicacion de la bodega sin caracteres especiales y de mas de 5 letras.")  # Mensaje de error
        return inputUbicacionBodega  # Devuelve el valor limpio si es válido
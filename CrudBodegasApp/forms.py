from django import forms
from CrudBodegasApp.models import Bodegas
import re

class BodegaRegistracionForm(forms.ModelForm):

    class Meta:
        model = Bodegas
        fields = '__all__'
        labels = {
            'NombreBodega': 'Nombre de la bodega',
            'UbicacionBodega': 'Ubicacion de la bodega',
        }
        help_texts = {
            'NombreBodega': 'Ingrese el nombre de la bodega',
            'UbicacionBodega': 'Indique la ubicacion de la bodega',
        }
        error_messages = {
            'NombreBodega': {
                'required': 'Por favor ingrese un nombre a la bodega',
            },
            'UbicacionBodega': {
                'required': 'Por favor ingrese la ubicacion de la bodega',
            },
        }
        widgets = {
            'NombreBodega': forms.TextInput(attrs={
                'placeholder': 'Ej: Bodega norte'
            }),
            'UbicacionBodega': forms.TextInput(attrs={
                'placeholder': 'Ej: Primer piso'
            }),
        }



        
    def clean_NombreBodega(self):
        inputNombreBodega = self.cleaned_data['NombreBodega'].strip().upper().title()  # Obtiene valor y elimina espacios al inicio y fin
        caracteres = r"^(?:\d+|[A-ZÁÉÍÓÚÑa-záéíóúñ]{2,})(?: (?:\d+|[A-ZÁÉÍÓÚÑa-záéíóúñ]{2,}))*$"
        query = Bodegas.objects.filter(NombreBodega=inputNombreBodega)

        if not re.match(caracteres, inputNombreBodega):  # Valida la longitud máxima
            raise forms.ValidationError("Ingrese un nombre de bodega sin caracteres especiales, con de mas de 5 letras, sin juntar numeros ni letras y no con mas de 1 espacio entre caracteres.")  # Mensaje de error
        if self.instance.pk:
            query = query.exclude(pk=self.instance.pk)
        if query.exists():
            raise forms.ValidationError("Este Nombre de Bodega ya está registrado.")
        return inputNombreBodega  # Devuelve el valor limpio si es válido
    
    def clean_UbicacionBodega(self):
        inputUbicacionBodega = self.cleaned_data['UbicacionBodega'].strip().upper().title()  # Obtiene valor y elimina espacios al inicio y fin
        caracteres = r"^(?:\d+|[A-ZÁÉÍÓÚÑa-záéíóúñ]{2,})(?: (?:\d+|[A-ZÁÉÍÓÚÑa-záéíóúñ]{2,}))*$"

        if not re.match(caracteres, inputUbicacionBodega):  # Valida la longitud máxima
            raise forms.ValidationError("Ingrese la ubicacion de la bodega sin caracteres especiales, con de mas de 5 letras, sin juntar numeros ni letras y no con mas de 1 espacio entre caracteres.")  # Mensaje de error
        return inputUbicacionBodega  # Devuelve el valor limpio si es válido
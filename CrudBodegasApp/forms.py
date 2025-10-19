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
            'EstadoBodega': 'Estado de la bodega',
            'ObservacionesBodega': 'Observaciones sobre la bodega',
        }
        help_texts = {
            'NombreBodega': 'Ingrese el nombre de la bodega',
            'UbicacionBodega': 'Indique la ubicacion de la bodega',
            'EstadoBodega': 'Seleccione el estado actual de la bodega (Activa, Inactiva o En Mantenimiento)',
            'ObservacionesBodega': 'Ingrese detalles adicionales o notas relevantes sobre la bodega',
        }
        error_messages = {
            'NombreBodega': {
                'required': 'Por favor ingrese un nombre a la bodega',
            },
            'UbicacionBodega': {
                'required': 'Por favor ingrese la ubicacion de la bodega',
            },
            'EstadoBodega': {
                'required': 'Debe seleccionar un estado para la bodega.',
            },
            'ObservacionesBodega': {
                'required': 'Por favor ingrese una observación o nota descriptiva.',
                'min_length': 'Las observaciones deben tener al menos 10 caracteres.',
            },
        }
        widgets = {
            'NombreBodega': forms.TextInput(attrs={
                'placeholder': 'Ej: Bodega norte'
            }),
            'UbicacionBodega': forms.TextInput(attrs={
                'placeholder': 'Ej: Primer piso'
            }),
            'EstadoBodega': forms.Select(attrs={
                'placeholder': 'Ej: Inactivo'
            }),
            'ObservacionesBodega': forms.Textarea(attrs={
                'placeholder': 'Ej: Se utiliza para productos perecibles o de rotación rápida.'
            }),
            
        }



        
    def clean_NombreBodega(self):
        inputNombreBodega = self.cleaned_data['NombreBodega'].strip().upper().title()  # Obtiene valor y elimina espacios al inicio y fin
        caracteres = r"^(?:\d+|[A-ZÁÉÍÓÚÑa-záéíóúñ]{2,})(?: (?:\d+|[A-ZÁÉÍÓÚÑa-záéíóúñ]{2,}))*$"

        if not re.match(caracteres, inputNombreBodega):  # Valida la longitud máxima
            raise forms.ValidationError("Ingrese un nombre de bodega sin caracteres especiales, con de mas de 5 letras, sin juntar numeros ni letras y no con mas de 1 espacio entre caracteres.")  # Mensaje de error
        return inputNombreBodega  # Devuelve el valor limpio si es válido
    
    def clean_UbicacionBodega(self):
        inputUbicacionBodega = self.cleaned_data['UbicacionBodega'].strip().upper().title()  # Obtiene valor y elimina espacios al inicio y fin
        caracteres = r"^(?:\d+|[A-ZÁÉÍÓÚÑa-záéíóúñ]{2,})(?: (?:\d+|[A-ZÁÉÍÓÚÑa-záéíóúñ]{2,}))*$"

        if not re.match(caracteres, inputUbicacionBodega):  # Valida la longitud máxima
            raise forms.ValidationError("Ingrese la ubicacion de la bodega sin caracteres especiales, con de mas de 5 letras, sin juntar numeros ni letras y no con mas de 1 espacio entre caracteres.")  # Mensaje de error
        return inputUbicacionBodega  # Devuelve el valor limpio si es válido
    
    def clean_ObservacionesBodega(self):
        inputObservacionesBodega = self.cleaned_data['ObservacionesBodega']
        
        if len(inputObservacionesBodega) < 10:
            raise forms.ValidationError("La observación debe tener al menos 10 caracteres.")
        if inputObservacionesBodega.isdigit():
            raise forms.ValidationError("La observación no puede contener solo números.")
        return inputObservacionesBodega
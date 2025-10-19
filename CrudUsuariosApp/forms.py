from django import forms
from CrudUsuariosApp.models import Usuarios
import re

class UsuarioRegistrationForm(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = '__all__'

        labels = {
            'Username': 'Nombre de usuario',
            'Password': 'Contraseña'
        }
        help_texts = {
            'Username': 'Asegúrese de usar letras y numeros',
            'Password': 'Debe usar minimo 1 letra y 1 numero'
        }
        error_messages = {
            'Username': {
                'required': 'Por favor introduzca el nombre de usuario',
                'max_length': 'El nombre de usuario no puede exceder el limite permitido',
            },
            'Password': {
                'required': 'Por favor introduzca una contraseña',
            }
        }
        widgets = {
            'Username': forms.TextInput(attrs={
                'placeholder': 'Ej: Pablo123'
            }),
            'Password': forms.TextInput(attrs={
                'placeholder': 'Ej: Pablo_68'
            })
        }


    def clean_Username(self):
        inputUsername = self.cleaned_data['Username'].strip().upper()  # Obtiene valor y elimina espacios al inicio y fin
        caracteres = r"^[a-zA-Z]{5,}$"
        
        query = Usuarios.objects.filter(Username=inputUsername)

        if not re.match(caracteres, inputUsername):  # Valida la longitud máxima
            raise forms.ValidationError("Ingrese un Usuario sin caracteres especiales de mas de 4 letras.")  # Mensaje de error
        if self.instance.pk:
            query = query.exclude(pk=self.instance.pk)
        if query.exists():
            raise forms.ValidationError("Este Usuario ya está registrado.")
        return inputUsername  # Devuelve el valor limpio si es válido
    


    def clean_Password(self):
        inputPassword = self.cleaned_data['Password'].strip()  # Obtiene valor y elimina espacios al inicio y fin
        caracteres = r'^(?=(?:[^A-Za-z]*[A-Za-z]){8,})(?=.*\d)(?=.*[!@#$%^&*()_+\-=\[\]{}|;:\'",.<>/?]).*$'

        if not re.match(caracteres, inputPassword):  # Valida la longitud máxima
            raise forms.ValidationError("Ingrese una contraseña valido con mas de 8 letras, 1 caracter especial y un numero.")  # Mensaje de error
        return inputPassword  # Devuelve el valor limpio si es válido
    
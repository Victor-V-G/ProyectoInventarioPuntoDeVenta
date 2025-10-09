from django import forms
from CrudUsuariosApp.models import Usuarios
import re

class UsuarioRegistrationForm(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = '__all__'

    def clean_Username(self):
        inputUsername = self.cleaned_data['Username'].strip().upper()  # Obtiene valor y elimina espacios al inicio y fin
        caracteres = r"^[a-zA-Z]{6,}$"

        if not re.match(caracteres, inputUsername):  # Valida la longitud máxima
            raise forms.ValidationError("Ingrese un Usuario sin caracteres especiales de mas de 5 letras.")  # Mensaje de error
        if Usuarios.objects.filter(Username=inputUsername).exists():
            raise forms.ValidationError("Este Usuario ya está registrado.")
        return inputUsername  # Devuelve el valor limpio si es válido
    
    def clean_Password(self):
        inputPassword = self.cleaned_data['Password'].strip()  # Obtiene valor y elimina espacios al inicio y fin
        caracteres = r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[!@#$%^&*()_+\-=\[\]{}|;:\'",.<>/?]).{8,}$'

        if not re.match(caracteres, inputPassword):  # Valida la longitud máxima
            raise forms.ValidationError("Ingrese una contraseña valido con mas de 8 letras, 1 caracter especial y un numero.")  # Mensaje de error
        return inputPassword  # Devuelve el valor limpio si es válido
    
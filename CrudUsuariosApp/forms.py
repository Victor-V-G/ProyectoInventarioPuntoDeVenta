from django import forms
from CrudUsuariosApp.models import Usuarios
import re

class UsuarioRegistrationForm(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = '__all__'

        labels = {
            'Username': 'Nombre de usuario',
            'Password': 'Contraseña',
            'ConfirmarPassword': 'Confirmar contraseña',
            'CorreoElectronico': 'Correo electrónico'
        }

        help_texts = {
            'Username': 'Ingrese su nombre de usuario.',
            'Password': 'La contraseña debe contener al menos 5 caracteres, debe contar con al menos 1 letra, 1 número',
            'ConfirmarPassword': 'Repita la misma contraseña para confirmar.',
            'CorreoElectronico': 'Ingrese un correo electrónico válido'
        }

        error_messages = {
            'Username': {
                'required': 'Por favor introduzca el nombre de usuario.',
                'max_length': 'El nombre de usuario no puede exceder el límite permitido.',
                'unique': 'Este nombre de usuario ya se encuentra registrado.',
            },
            'Password': {
                'required': 'Por favor introduzca una contraseña.',
                'min_length': 'La contraseña debe tener al menos 5 caracteres.'
            },
            'ConfirmarPassword': {
                'required': 'Debe confirmar su contraseña.',
                'min_length': 'La contraseña debe tener al menos 5 caracteres.'
            },
            'CorreoElectronico': {
                'required': 'Por favor introduzca su correo electrónico.',
                'invalid': 'Ingrese un correo electrónico válido.',
                'unique': 'El correo electrónico ingresado ya está en uso.'
            }
        }

        widgets = {
            'Username': forms.TextInput(attrs={
                'placeholder': 'Ej: Pablo123',
            }),
            'Password': forms.PasswordInput(attrs={
                'placeholder': 'Ej: Pablo_68',
            }),
            'ConfirmarPassword': forms.PasswordInput(attrs={
                'placeholder': 'Repita su contraseña',
            }),
            'CorreoElectronico': forms.EmailInput(attrs={
                'placeholder': 'Ej: usuario@gmail.com',
            })
        }


    def clean_Username(self):
        inputUsername = self.cleaned_data['Username']
        caracteres = r'^[A-Za-z0-9_-]{5,}$'
        if not re.match(caracteres, inputUsername):
            raise forms.ValidationError("El nombre de usuario debe tener al menos 5 caracteres y solo puede contener letras, números, guiones (-) o guiones bajos (_), sin espacios.")
        return inputUsername


    def clean_Username(self):
        inputUsername = self.cleaned_data['Username']
        if inputUsername.isdigit():
            raise forms.ValidationError("El nombre de usuario no puede estar compuesto solo por números.")
        return inputUsername


    def clean_Password(self):
        inputPassword = self.cleaned_data['Password'].strip()  # Quita espacios
        caracteres = r'^(?=.*[A-Za-z])(?=.*\d).{5,}$'
        if not re.match(caracteres, inputPassword):
            raise forms.ValidationError("La contraseña debe tener al menos 5 caracteres, incluyendo al menos una letra y un número.")
        return inputPassword
    

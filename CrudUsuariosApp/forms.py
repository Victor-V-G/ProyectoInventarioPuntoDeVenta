from django import forms
from CrudUsuariosApp.models import Usuarios
import re
from django.contrib.auth.hashers import make_password

# Formulario para registrar usuarios basado en el modelo Usuarios
class UsuarioRegistrationForm(forms.ModelForm):
    ConfirmarPassword = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Repita su contraseña'}),
        label="Confirmar contraseña"
    )

    class Meta:
        model = Usuarios  # Modelo en el que se basa el formulario
        fields = ['Username', 'Password', 'ConfirmarPassword', 'CorreoElectronico']  # Incluye todos los campos del modelo

        # Etiquetas visibles en el formulario
        labels = {
            'Username': 'Nombre de usuario',
            'Password': 'Contraseña',
            'ConfirmarPassword': 'Confirmar contraseña',
            'CorreoElectronico': 'Correo electrónico'
        }

        # Ayudas que aparecen junto a los campos
        help_texts = {
            'Username': 'Ingrese su nombre de usuario.',
            'Password': 'La contraseña debe contener al menos 5 caracteres, debe contar con al menos 1 letra, 1 número',
            'ConfirmarPassword': 'Repita la misma contraseña para confirmar.',
            'CorreoElectronico': 'Ingrese un correo electrónico válido'
        }

        # Mensajes de error personalizados
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

        # Widgets para personalizar el HTML de cada campo
        widgets = {
            'Username': forms.TextInput(attrs={'placeholder': 'Ej: Pablo123'}),
            'Password': forms.PasswordInput(attrs={'placeholder': 'Ej: Pablo_68'}),
            'ConfirmarPassword': forms.PasswordInput(attrs={'placeholder': 'Repita su contraseña'}),
            'CorreoElectronico': forms.EmailInput(attrs={'placeholder': 'Ej: usuario@gmail.com'}),
        }

    # ====================================================================
    # Validaciones personalizadas por campo
    # ====================================================================

    # Valida que el nombre de usuario tenga al menos 5 caracteres y solo contenga letras, números, guiones o guiones bajos
    def clean_Username(self):
        inputUsername = self.cleaned_data['Username']
        caracteres = r'^[A-Za-z0-9_-]{5,}$'

        if not re.match(caracteres, inputUsername):
            raise forms.ValidationError(
                "El nombre de usuario debe tener al menos 5 caracteres y solo puede contener letras, números, guiones (-) o guiones bajos (_), sin espacios."
            )

        # Valida que el nombre de usuario no sea solo números
        if inputUsername.isdigit():
            raise forms.ValidationError("El nombre de usuario no puede estar compuesto solo por números.")
        
        return inputUsername

    # Valida que la contraseña tenga al menos 5 caracteres y contenga al menos una letra y un número
    def clean_Password(self):
        inputPassword = self.cleaned_data['Password'].strip()  # Quita espacios
        caracteres = r'^(?=.*[A-Za-z])(?=.*\d).{5,}$'

        if not re.match(caracteres, inputPassword):
            raise forms.ValidationError(
                "La contraseña debe tener al menos 5 caracteres, incluyendo al menos una letra y un número."
            )

        return inputPassword
    

    def clean(self):
        cleaned_data = super().clean()
        Password = cleaned_data.get("Password")
        ConfirmarPassword = cleaned_data.get("ConfirmarPassword")

        if Password != ConfirmarPassword:
            raise forms.ValidationError("Las contraseñas no coinciden")
        
        cleaned_data["Password"] = make_password(Password)
    
        return cleaned_data

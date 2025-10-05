from django import forms
from CrudUsuariosApp.models import Usuarios

class UsuarioRegistrationForm(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = '__all__'
from django import forms
from CrudUsuariosApp.models import Usuarios
import re
from django.contrib.auth.hashers import make_password
from CrudEmpleadosApp.models import Empleados ##Para usar con llaves foraneas
from CrudCargosApp.models import Cargos ##Para usar con llaves foraneas

# Formulario para registrar usuarios basado en el modelo Usuarios
class UsuarioRegistrationForm(forms.ModelForm):
    ConfirmarPassword = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Repita su contraseña'}),
        label="Confirmar contraseña"
    )

    class Meta:
        model = Usuarios  # Modelo en el que se basa el formulario
        fields = ['Username','CorreoElectronico','Empleado','Cargo','Password','ConfirmarPassword',]

        # Etiquetas visibles en el formulario
        labels = {
            'Username': 'Nombre de usuario',
            'Password': 'Contraseña',
            'ConfirmarPassword': 'Confirmar contraseña',
            'CorreoElectronico': 'Correo electrónico',
            'Empleado': 'Empleado seleccionado',
            'Cargo': 'Cargo seleccionado'
        }

        # Ayudas que aparecen junto a los campos
        help_texts = {
            'Username': 'Ingrese su nombre de usuario.',
            'Password': 'La contraseña debe contener al menos 5 caracteres, debe contar con al menos 1 letra, 1 número',
            'ConfirmarPassword': 'Repita la misma contraseña para confirmar.',
            'CorreoElectronico': 'Ingrese un correo electrónico válido',
            'Empleado': 'Seleccione el Empleado del Usuario (Previamente registrado.)',
            'Cargo': 'Seleccione el Cargo del Usuario (Previamente registrado.)',
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
                'min_length': 'La contraseña debe tener al menos 5 caracteres.',
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
        query = Usuarios.objects.filter(Username=inputUsername)  # Verifica duplicados

        # Si es actualización, excluye el propio registro
        if self.instance.pk:
            query = query.exclude(pk=self.instance.pk)
        if not re.match(caracteres, inputUsername):
            raise forms.ValidationError(
                "El nombre de usuario debe tener al menos 5 caracteres y solo puede contener letras, números, guiones (-) o guiones bajos (_), sin espacios."
            )
        # Valida duplicados
        if query.exists():
            raise forms.ValidationError("Este usuario ya está registrado.")
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

    ###VALIDACION FOREIGN KEY
    def clean_Empleado(self):
        # Obtiene el empleado seleccionado
        ExisteEmpleado = self.cleaned_data.get('Empleado')
        query = Usuarios.objects.filter(Empleado=ExisteEmpleado)  # Verifica duplicados
        # Si no existen empleados registrados en la BD
        if not Empleados.objects.exists():
            raise forms.ValidationError("Debes registrar al menos un empleado para poder seleccionar uno.")
        # Si el usuario no seleccionó ninguna empleado
        if self.instance.pk:
            query = query.exclude(pk=self.instance.pk)
        if query.exists():
            raise forms.ValidationError("Este Empleado ya esta en uso.")
        if ExisteEmpleado is None:
            raise forms.ValidationError("Debes seleccionar un empleado.")
        # Retorna la categoría válida
        return ExisteEmpleado
    
    def clean_Cargo(self):
        # Obtiene el cargo seleccionado
        ExisteCargo = self.cleaned_data.get('Cargo')
        # Si no cargos registrados en la BD
        if not Cargos.objects.exists():
            raise forms.ValidationError("Debes registrar al menos un cargo para poder seleccionar uno.")
        # Si el usuario no seleccionó ninguna cargo
        if ExisteCargo is None:
            raise forms.ValidationError("Debes seleccionar un cargo.")
        # Retorna la categoría válida
        return ExisteCargo
    
    def __init__(self, *args, **kwargs):
        # Llama al constructor original del formulario
        super().__init__(*args, **kwargs)
        
        # Configura el campo de empleado para que muestre todos los empleados disponibles
        self.fields['Empleado'].queryset = Empleados.objects.all()
        # Define cómo se mostrará cada empleado en el desplegable (usa su nombre)
        self.fields['Empleado'].label_from_instance = lambda obj: f"{obj.NombreEmpleado} {obj.ApellidoEmpleado} - RUT: {obj.RutEmpleado}"
        # Establece una etiqueta por defecto cuando no se ha seleccionado un empleado
        self.fields['Empleado'].empty_label = "Seleccione un empleado existente."

        # Configura el campo de cargo para que muestre todos los empleados disponibles
        self.fields['Cargo'].queryset = Cargos.objects.all()
        # Define cómo se mostrará cada cargo en el desplegable (usa su nombre)
        self.fields['Cargo'].label_from_instance = lambda obj: f"{obj.TipoDeCargo} - Descripcion: {obj.DescripcionDelCargo}"
        # Establece una etiqueta por defecto cuando no se ha seleccionado un cargo
        self.fields['Cargo'].empty_label = "Seleccione un cargo existente."


class UsuarioUpdateForm(forms.ModelForm):
    # Checkbox para indicar si se desea cambiar la contraseña
    CambiarPassword = forms.BooleanField(
        required=False,
        label="Cambiar contraseña"
    )
    # Campo para la nueva contraseña
    Password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Nueva contraseña'}),
        required=False,
        label="Nueva contraseña"
    )
    # Campo para confirmar la nueva contraseña
    ConfirmarPassword = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirmar contraseña'}),
        required=False,
        label="Confirmar contraseña"
    )

    class Meta:
        model = Usuarios
        fields = ['Username', 'CorreoElectronico', 'Empleado', 'Cargo']

        labels = {
            'Username': 'Nombre de usuario',
            'CorreoElectronico': 'Correo electrónico',
            'Empleado': 'Empleado seleccionado',
            'Cargo': 'Cargo seleccionado'
        }

        # Ayudas para los campos
        help_texts = {
            'Username': 'Ingrese su nombre de usuario.',
            'CorreoElectronico': 'Ingrese un correo electrónico válido',
            'Cargo': 'Seleccione el Cargo del Usuario (Previamente registrado.)',
        }

        # Mensajes de error personalizados
        error_messages = {
            'Username': {
                'required': 'Por favor introduzca el nombre de usuario.',
                'max_length': 'El nombre de usuario no puede exceder el límite permitido.',
                'unique': 'Este nombre de usuario ya se encuentra registrado.',
            },
            'CorreoElectronico': {
                'required': 'Por favor introduzca su correo electrónico.',
                'invalid': 'Ingrese un correo electrónico válido.',
                'unique': 'El correo electrónico ingresado ya está en uso.'
            }
        }

        # Widgets para personalizar el HTML
        widgets = {
            'Username': forms.TextInput(attrs={'placeholder': 'Ej: Pablo123'}),
            'CorreoElectronico': forms.EmailInput(attrs={'placeholder': 'Ej: usuario@gmail.com'}),
        }

    # Validación del campo Username
    def clean_Username(self):
        inputUsername = self.cleaned_data['Username']
        caracteres = r'^[A-Za-z0-9_-]{5,}$'
        query = Usuarios.objects.filter(Username=inputUsername)

        # Excluir el propio registro en actualización
        if self.instance.pk:
            query = query.exclude(pk=self.instance.pk)

        # Validar formato
        if not re.match(caracteres, inputUsername):
            raise forms.ValidationError(
                "El nombre de usuario debe tener al menos 5 caracteres y solo puede contener letras, números, guiones (-) o guiones bajos (_), sin espacios."
            )

        # Validar duplicados
        if query.exists():
            raise forms.ValidationError("Este usuario ya está registrado.")

        # Validar que no sea solo números
        if inputUsername.isdigit():
            raise forms.ValidationError("El nombre de usuario no puede estar compuesto solo por números.")
        
        return inputUsername

    # Validación general del formulario (contraseñas)
    def clean(self):
        cleaned_data = super().clean()
        cambiar = cleaned_data.get("CambiarPassword")
        nuevaPassword = cleaned_data.get("Password")
        confirmarPassword = cleaned_data.get("ConfirmarPassword")
        caracteres = r'^(?=.*[A-Za-z])(?=.*\d).{5,}$'

        # Solo valida si se marcó el checkbox
        if cambiar:
            if not nuevaPassword or not confirmarPassword:
                raise forms.ValidationError("Debe ingresar y confirmar la nueva contraseña.")
            if nuevaPassword != confirmarPassword:
                raise forms.ValidationError("Las contraseñas no coinciden.")
            if not re.match(caracteres, nuevaPassword):
                raise forms.ValidationError(
                    "La contraseña debe tener al menos 5 caracteres, incluyendo una letra y un número."
                )
        return cleaned_data

    # Guarda el formulario, aplicando el cambio de contraseña si corresponde
    def save(self, commit=True):
        user = super().save(commit=False)
        cambiar = self.cleaned_data.get("CambiarPassword")
        nueva = self.cleaned_data.get("Password")

        if cambiar and nueva:
            user.Password = make_password(nueva)  # Hashea la contraseña

        if commit:
            user.save()
        return user

    # Validación del campo Cargo
    def clean_Cargo(self):
        ExisteCargo = self.cleaned_data.get('Cargo')
        if not Cargos.objects.exists():
            raise forms.ValidationError("Debes registrar al menos un cargo para poder seleccionar uno.")
        if ExisteCargo is None:
            raise forms.ValidationError("Debes seleccionar un cargo.")
        return ExisteCargo

    # Inicialización del formulario
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Empleado'].disabled = True  # No permitir cambios en empleado
        self.fields['Cargo'].queryset = Cargos.objects.all()
        self.fields['Cargo'].label_from_instance = lambda obj: f"{obj.TipoDeCargo} - {obj.DescripcionDelCargo}"
        self.fields['Cargo'].empty_label = "Seleccione un cargo existente."
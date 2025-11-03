# ------------------------------------------------------------------------
# Importación de módulos y clases necesarias para el modelo
# ------------------------------------------------------------------------
# models: Permite definir clases que representan tablas de la base de datos.
# UniqueConstraint: Define restricciones de unicidad a nivel de tabla.
# MinLengthValidator: Valida que el texto tenga una longitud mínima.
# ValidationError: Se utiliza para lanzar errores personalizados en validaciones.
# re: Módulo de expresiones regulares, usado para verificar formatos de texto.
# ------------------------------------------------------------------------
from django.db import models
from django.db.models import UniqueConstraint
from django.core.validators import MinLengthValidator, EmailValidator
from django.core.exceptions import ValidationError
import re


# ========================================================================
# Modelo: Usuarios
# ========================================================================
# Este modelo representa la tabla 'Usuarios' en la base de datos.
# Se utiliza db_column para mapear cada campo del modelo a su columna
# existente, evitando que Django cree nuevas columnas con nombres automáticos.
# ========================================================================
class Usuarios(models.Model):

    # --------------------------------------------------------------------
    # ID del usuario
    # --------------------------------------------------------------------
    # AutoField: campo autoincremental que genera un identificador único.
    # primary_key=True: define este campo como clave primaria.
    # db_column: nombre exacto de la columna en la base de datos.
    # --------------------------------------------------------------------
    IdUsuarios = models.AutoField(
        primary_key=True, 
        db_column='IdUsuarios'
    )
    # --------------------------------------------------------------------


    # --------------------------------------------------------------------
    # Nombre de usuario (Username)
    # --------------------------------------------------------------------
    # CharField: campo de texto que almacena el nombre de usuario.
    # max_length: longitud máxima de 30 caracteres.
    # validators: valida que el nombre tenga al menos 5 caracteres.
    # db_column: nombre exacto de la columna en la base de datos.
    # error_messages: mensaje personalizado si el nombre ya existe (único).
    # --------------------------------------------------------------------
    Username = models.CharField(
        max_length=30, 
        db_column='Username',
        validators=[MinLengthValidator(5, message="El username debe tener al menos 5 caracteres")],
        error_messages={'unique': 'El username ingresado ya se encuentra ocupado, Por favor, intentelo con otro nuevamente.'}
    )
    # --------------------------------------------------------------------


    # --------------------------------------------------------------------
    # FUNCIÓN: validacion_password_segura
    # --------------------------------------------------------------------
    # Esta función valida que la contraseña cumpla con los requisitos mínimos
    # de seguridad:
    #  - Contenga al menos una letra (mayúscula o minúscula)
    #  - Contenga al menos un número
    # Se utiliza una expresión regular (regex) para verificarlo.
    # Si la validación falla, lanza un ValidationError con un mensaje descriptivo.
    # --------------------------------------------------------------------
    def validacion_password_segura(value):
        expresion = r'^(?=.*[a-zA-Z])(?=.*[0-9]).*$'
        if re.search(expresion, value):
            return value
        else:
            raise ValidationError('La password ingresada debe contener al menos 1 letra y 1 numero')
    # --------------------------------------------------------------------


    # --------------------------------------------------------------------
    # Contraseña del usuario
    # --------------------------------------------------------------------
    # CharField: almacena el texto de la contraseña (en texto plano o encriptado).
    # max_length: longitud máxima de 45 caracteres.
    # validators:
    #   - validacion_password_segura: asegura complejidad mínima.
    #   - MinLengthValidator: obliga a tener al menos 5 caracteres.
    # db_column: mapea al campo real en la base de datos.
    # --------------------------------------------------------------------
    Password = models.CharField(
        max_length=128, 
        db_column='Password',
        validators=[
            validacion_password_segura,
            MinLengthValidator(5, message="La password debe tener al menos 5 caracteres")
        ]
    )
    # --------------------------------------------------------------------

    # ============================================================
    # Validación general del formulario
    # ============================================================
    # Este método se llama automáticamente después de validar los campos individuales.
    # Sirve para realizar validaciones que dependan de más de un campo.
    def clean(self): 
        super().clean()  # Llama a la limpieza y validación base del formulario
    
        # Valida que los campos Password y ConfirmarPassword coincidan
        if self.Password != self.ConfirmarPassword:
            raise ValidationError({
                'ConfirmarPassword': 'Las passwords ingresadas no coinciden'
            })


    # ============================================================
    # Campo para confirmar la contraseña ingresada por el usuario
    # ============================================================
    ConfirmarPassword = models.CharField(
        max_length=128,  # Limita la longitud máxima de la contraseña
        db_column='ConfirmarPassword',  # Nombre de la columna en la base de datos
        verbose_name='Confirmar password',  # Etiqueta legible en el admin y formularios
        validators=[
            MinLengthValidator(5, message="La password debe tener al menos 5 caracteres")
        ]  # Valida que tenga al menos 5 caracteres
    )


    # ============================================================
    # Campo de correo electrónico
    # ============================================================
    CorreoElectronico = models.EmailField(
        max_length=100,  # Longitud máxima permitida
        db_column='CorreoElectronico',  # Nombre de columna en la base de datos
        verbose_name='Correo electronico',  # Etiqueta legible en el admin y formularios
        validators=[EmailValidator(message="Debe ingresar un correo valido")],  # Valida formato de correo
        error_messages={
            'unique': 'El correo electronico ingresado ya se encuentra ocupado, Por favor, intentelo con otro nuevamente.'
        }  # Mensaje personalizado si el correo ya existe
    )


    # --------------------------------------------------------------------
    # Meta información del modelo
    # --------------------------------------------------------------------
    # Clase interna que define configuraciones adicionales del modelo:
    #  - db_table: nombre exacto de la tabla en la base de datos.
    #  - constraints: restricciones de unicidad para campos específicos.
    #    Evita que se repitan IDs o usernames dentro de la tabla.
    # --------------------------------------------------------------------
    class Meta:
        db_table = 'Usuarios'
        constraints = [
            UniqueConstraint(fields=['IdUsuarios'], name='unique_id_usuarios'),
            UniqueConstraint(fields=['Username'], name='unique_username'),
            UniqueConstraint(fields=['CorreoElectronico'], name='unique_correo_electronico'),
        ]
    # --------------------------------------------------------------------


    # --------------------------------------------------------------------
    # MÉTODO __STR__ IMPLEMENTADO
    # --------------------------------------------------------------------
    # Devuelve una representación legible del objeto.
    # Es útil al mostrar registros en el panel de administración de Django
    # o en la consola interactiva. Muestra los datos más importantes del usuario.
    # --------------------------------------------------------------------
    def __str__(self):
        return f"ID: {self.IdUsuarios}, USERNAME: {self.Username}, PASSWORD: {self.Password} CORREO ELECTRONICO: {self.CorreoElectronico}"

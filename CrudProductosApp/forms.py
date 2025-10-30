# Importaciones necesarias
from django import forms  # Importa el módulo de formularios de Django
from CrudProductosApp.models import Productos  # Importa el modelo Producto
import re
from datetime import date
from bootstrap_datepicker_plus.widgets import DatePickerInput #Importacion de wiget de fehc

# ========================================================================
# Formulario: Registro de Productos
# ========================================================================
# Este formulario permite crear o actualizar registros de productos
# usando el modelo Producto. Al heredar de ModelForm, genera automáticamente
# campos basados en el modelo.
# ========================================================================

# Formulario para registrar productos basado en el modelo Productos
class ProductoRegistrationForm(forms.ModelForm):

    # Campo personalizado de fecha de vencimiento con formato DD-MM-YYYY
    FechaDeVencimiento = forms.DateField(
        input_formats=['%d-%m-%Y'],  # Formato de entrada esperado
        label='Fecha de vencimiento',
        help_text='Indique la fecha de vencimiento mencionada en el producto (DD-MM-YYYY).',
        error_messages={
            'required': 'Por favor introduzca la fecha de vencimiento del producto',
            'invalid': 'Ingrese una fecha válida en formato DD-MM-YYYY.'
        },
        widget=forms.DateInput(
            format='%d-%m-%Y',
            attrs={'placeholder': 'DD-MM-YYYY', 'type': 'date'}  # Tipo text para permitir máscara
        )
    )

    class Meta:
        model = Productos  # Modelo al que está vinculado el formulario
        fields = '__all__'  # Incluye todos los campos del modelo

        # Etiquetas visibles en el formulario
        labels = {
            'CodigoDeBarras': 'Codigo de barras',
            'ValorProducto': 'Valor',
            'StockProducto': 'Stock',
            'NombreProducto': 'Nombre del producto',
            'MarcaProducto': 'Marca del producto',
        }

        # Ayudas que aparecen junto a los campos
        help_texts = {
            'CodigoDeBarras': 'Indique el codigo de barras del producto a registrar',
            'ValorProducto': 'El valor aceptado es a partir de $1000',
            'StockProducto': 'No esta permitido registrar el producto sin stock',
            'NombreProducto': 'Ingrese el nombre tal cual muestra el producto',
            'MarcaProducto': 'Indique la marca la cual pertenece el producto',
        }

        # Mensajes de error personalizados
        error_messages = {
            'CodigoDeBarras': {
                'required': 'Por favor introduzca el codigo de barras',
                'unique': 'Este codigo de barras ya esta registrado',
                'invalid': 'Ingrese solamente numeros y sin espacios',
            },
            'ValorProducto': {
                'required': 'Por favor introduzca el valor del producto',
                'invalid': 'Ingrese un valor valido',
            },
            'StockProducto': {
                'required': 'Por favor introduzca el stock del producto',
                'invalid': 'Ingrese un stock valido',
            },
            'NombreProducto': {
                'required': 'Por favor introduzca el nombre del producto',
            },
            'MarcaProducto': {
                'required': 'Por favor introduzca la marca del producto',
            },
        }

        # Widgets para personalizar el HTML de cada campo
        widgets = {
            'CodigoDeBarras': forms.TextInput(attrs={'placeholder': 'Ej: 7802900000328'}),
            'ValorProducto': forms.NumberInput(attrs={'placeholder': 'Ej: $1500'}),
            'StockProducto': forms.NumberInput(attrs={'placeholder': 'Ej: 5 (unidades)'}),
            'NombreProducto': forms.TextInput(attrs={'placeholder': 'Ej: Papas fritas'}),
            'MarcaProducto': forms.TextInput(attrs={'placeholder': 'Ej: Fruna'}),
        }

    # ====================================================================
    # Validaciones personalizadas por campo
    # ====================================================================

    # Valida que el código de barras sea solo números y único
    def clean_CodigoDeBarras(self):
        inputCodigoDeBarras = self.cleaned_data['CodigoDeBarras']
        expresion = r'^[0-9]+$'
        query = Productos.objects.filter(CodigoDeBarras=inputCodigoDeBarras)

        if not re.match(expresion, inputCodigoDeBarras):
            raise forms.ValidationError("Ingrese solamente numeros y sin espacios")
        if self.instance.pk:
            query = query.exclude(pk=self.instance.pk)  # Excluye el registro actual si es edición
        if query.exists():
            raise forms.ValidationError("Este Codigo de Barras ya está registrado.")
        return inputCodigoDeBarras

    # Valida que el valor del producto sea positivo y mínimo 3 dígitos
    def clean_ValorProducto(self):
        inputValorProducto = self.cleaned_data['ValorProducto']

        if inputValorProducto < 0:
            raise forms.ValidationError("No puede ingresar valores negativos")
        if len(str(inputValorProducto)) < 3:
            raise forms.ValidationError("Debe ingresar un valor valido a partir de 3 digitos ($123)")
        if inputValorProducto == 0:
            raise forms.ValidationError("El valor no puede ser 0")
        return inputValorProducto

    # Valida que el stock sea positivo y mayor a 0
    def clean_StockProducto(self):
        inputStockProducto = self.cleaned_data['StockProducto']

        if inputStockProducto < 0:
            raise forms.ValidationError("No puede ingresar stock negativos")
        if inputStockProducto == 0:
            raise forms.ValidationError("El Stock no puede ser 0")
        return inputStockProducto

    # Valida que el nombre del producto no contenga caracteres especiales y tenga formato correcto
    def clean_NombreProducto(self):
        inputNombreProducto = self.cleaned_data['NombreProducto'].strip()
        caracteres = r'^[A-Za-zÁÉÍÓÚÑáéíóúñ]+(?: [A-Za-zÁÉÍÓÚÑáéíóúñ]+)*(?: \d+[gG]?)?$'

        if not re.match(caracteres, inputNombreProducto):
            raise forms.ValidationError(
                "Ingrese un nombre del producto sin caracteres especiales, con de mas de 5 letras, "
                "sin juntar numeros ni letras y no con mas de 1 espacio entre caracteres."
            )
        return inputNombreProducto

    # Valida que la fecha de vencimiento sea posterior a la fecha actual
    def clean_FechaDeVencimiento(self):
        inputFechaDeVencimiento = self.cleaned_data['FechaDeVencimiento']

        if not inputFechaDeVencimiento:
            raise forms.ValidationError("Debe ingresar una fecha de vencimiento.")
        
        fecha_actual = date.today()
        if inputFechaDeVencimiento < fecha_actual:
            raise forms.ValidationError("La fecha de vencimiento no puede ser anterior a la fecha actual.")

        return inputFechaDeVencimiento

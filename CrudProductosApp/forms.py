# Importaciones necesarias
from django import forms  # Importa el módulo de formularios de Django
from CrudProductosApp.models import Productos  # Importa el modelo Producto
import re
from datetime import date

# ========================================================================
# Formulario: Registro de Productos
# ========================================================================
# Este formulario permite crear o actualizar registros de productos
# usando el modelo Producto. Al heredar de ModelForm, genera automáticamente
# campos basados en el modelo.
# ========================================================================

class ProductoRegistrationForm(forms.ModelForm):
    FechaDeVencimiento = forms.DateField(
        label='Fecha de Vencimiento',
        input_formats=['%d-%m-%Y'],
        widget=forms.DateInput(
            format='%d-%m-%Y',  # <-- Esto es clave
            attrs={'placeholder': 'DD-MM-YYYY'}
        ),
        error_messages={'invalid': 'Ingrese una fecha válida en formato DD-MM-YYYY.'}
    )

    """
    Formulario para registrar o actualizar productos.
    Hereda de forms.ModelForm, lo que permite mapear los campos del modelo automáticamente.
    """

    class Meta:
        model = Productos  # Modelo en el que se basa el formulario
        fields = '__all__'  # Incluye todos los campos del modelo en el formulario

    def clean_CodigoDeBarras(self):
        inputCodigoDeBarras = self.cleaned_data['CodigoDeBarras']

        expresion = r'^[0-9]+$'
        query = Productos.objects.filter(CodigoDeBarras=inputCodigoDeBarras)

        if not re.match(expresion, inputCodigoDeBarras):
            raise forms.ValidationError("Ingrese solamente numeros y sin espacios")
        if self.instance.pk:
            query = query.exclude(pk=self.instance.pk)
        if query.exists():
            raise forms.ValidationError("Este Codigo de Barras ya está registrado.")
        return inputCodigoDeBarras
    

    def clean_ValorProducto(self):
        inputValorProducto = self.cleaned_data['ValorProducto']

        if inputValorProducto < 0:
            raise forms.ValidationError("No puede ingresar valores negativos")
        if len(str(inputValorProducto)) < 3:
            raise forms.ValidationError("Debe ingresar un valor valido a partir de 3 digitos ($123)")
        if inputValorProducto == 0 :
            raise forms.ValidationError("El valor no puede ser 0")
        return inputValorProducto
    

    def clean_StockProducto(self):
        inputStockProducto = self.cleaned_data['StockProducto']

        if inputStockProducto < 0:
            raise forms.ValidationError("No puede ingresar stock negativos")
        if inputStockProducto == 0 :
            raise forms.ValidationError("El Stock no puede ser 0")
        return inputStockProducto


    def clean_NombreProducto(self):
        inputNombreProducto = self.cleaned_data['NombreProducto'].strip()
        caracteres = r'^[A-Za-zÁÉÍÓÚÑáéíóúñ]+(?: [A-Za-zÁÉÍÓÚÑáéíóúñ]+)*(?: \d+[gG]?)?$'

        if not re.match(caracteres, inputNombreProducto):
            raise forms.ValidationError("Ingrese un nombre del producto sin caracteres especiales, con de mas de 5 letras, sin juntar numeros ni letras y no con mas de 1 espacio entre caracteres.")
        return inputNombreProducto


    def clean_FechaDeVencimiento(self):
        inputFechaDeVencimiento = self.cleaned_data['FechaDeVencimiento']

        # Verifica que se haya ingresado una fecha
        if not inputFechaDeVencimiento:
            raise forms.ValidationError("Debe ingresar una fecha de vencimiento.")
        
        fecha_actual = date.today()

        if inputFechaDeVencimiento < fecha_actual:
            raise forms.ValidationError("La fecha de vencimiento no puede ser anterior a la fecha actual.")
        return inputFechaDeVencimiento

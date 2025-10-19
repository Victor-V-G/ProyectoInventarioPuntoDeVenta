from django import forms
from CrudCategoriaProductoApp.models import CategoriaProducto

class CategoriaProductoRegistracionForm(forms.ModelForm):

    class Meta:
        model = CategoriaProducto
        fields = '__all__'
        labels = {
            'NombreCategoria': 'Nombre de la categoria',
            'Descripcion': 'Descripcion',
        }
        help_texts = {
            'NombreCategoria': 'Indique el nombre de la categoria a registrar',
            'Descripcion': 'Ingrese la descripcion sobre la categoria a registrar',
        }
        error_messages = {
            'NombreCategoria': {
                'required': 'Por favor introduzca un nombre a la categoria',
            },
            'Descripcion': {
                'required': 'Por favor ingrese una descripcion a la categoria a registrar',
            },
        }
        widgets = {
            'NombreCategoria': forms.TextInput(attrs={
                'placeholder': 'Ej: Snacks'
            }),
            'Descripcion': forms.TextInput(attrs={
                'placeholder': 'Ej: Categoría destinada a productos de consumo inmediato o ligero'
            }),
        }
    


    def clean_NombreCategoria(self):
        inputNombre = self.cleaned_data['NombreCategoria']
        if len(inputNombre) > 5:
            raise forms.ValidationError("El largo del nombre debe ser mas de 5 caracteres")
        return inputNombre
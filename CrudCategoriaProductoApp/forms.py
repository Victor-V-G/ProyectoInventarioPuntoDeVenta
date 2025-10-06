from django import forms
from CrudCategoriaProductoApp.models import CategoriaProducto

class CategoriaProductoRegistracionForm(forms.ModelForm):

    class Meta:
        model = CategoriaProducto
        fields = '__all__'

    def clean_NombreCategoria(self):
        inputNombre = self.cleaned_data['NombreCategoria']
        if len(inputNombre) > 5:
            raise forms.ValidationError("El largo del nombre debe ser mas de 5 caracteres")
        return inputNombre
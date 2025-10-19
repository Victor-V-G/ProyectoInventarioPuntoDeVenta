from django import forms
from CrudCategoriaProductoApp.models import CategoriaProducto

class CategoriaProductoRegistracionForm(forms.ModelForm):

    class Meta:
        model = CategoriaProducto
        fields = '__all__'
        labels = {
            'NombreCategoria': 'Nombre de la categoria',
            'Descripcion': 'Descripcion',
            'Estado': 'Estado de la categoría',
            'Observaciones': 'Observaciones'
        }
        help_texts = {
            'NombreCategoria': 'Indique el nombre de la categoria a registrar',
            'Descripcion': 'Ingrese la descripcion sobre la categoria a registrar',
            'Estado': 'Seleccione si la categoría está actualmente activa o pausada.',
            'Observaciones': 'Incluya cualquier detalle adicional o nota administrativa relevante.'
        }
        error_messages = {
            'NombreCategoria': {
                'required': 'Por favor introduzca un nombre a la categoria',
            },
            'Descripcion': {
                'required': 'Por favor ingrese una descripcion a la categoria a registrar',
            },
            'Estado': {
                'required': 'Debe seleccionar un estado para la categoría.'
            },
            'Observaciones': {
                'required': 'Por favor ingrese una observación o comentario.',
                'min_length': 'Las observaciones deben tener al menos 10 caracteres.'
            }
        }
        widgets = {
            'NombreCategoria': forms.TextInput(attrs={
                'placeholder': 'Ej: Snacks'
            }),
            'Descripcion': forms.Textarea(attrs={
                'placeholder': 'Ej: Categoría destinada a productos de consumo inmediato o ligero'
            }),
            'Estado': forms.Select(attrs={
                'placeholder': 'Ej: Inactivo'
            }),
            'Observaciones': forms.Textarea(attrs={
                'placeholder': 'Ej: Esta categoría se usa para productos exhibidos en mostrador.',
            })
        }
    

    def clean_NombreCategoria(self):
        inputNombre = self.cleaned_data['NombreCategoria']
        if len(inputNombre) < 3:
            raise forms.ValidationError("El largo del nombre de la categoria debe ser mas de 3 caracteres")
        return inputNombre
    

    def clean_Descripcion(self):
        inputDescripcion = self.cleaned_data['Descripcion'].strip()
        if len(inputDescripcion) < 10:
            raise forms.ValidationError("La descripción debe tener al menos 10 caracteres.")
        return inputDescripcion


    def clean_Observaciones(self):
        inputObservaciones = self.cleaned_data['Observaciones'].strip()
        if len(inputObservaciones) < 10:
            raise forms.ValidationError("Las observaciones deben tener al menos 10 caracteres.")
        return inputObservaciones
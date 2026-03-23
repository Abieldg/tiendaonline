from django import forms
from GestionProductos.models import Categoria



class FormularioContacto(forms.Form):
    nombre = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control col-md-6 mb-3',
            }
        )
    )
    correo=forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class':'form-control h-50',
            }
        )
    )
    comentario=forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class':'form-control h-50',
                
            }
        )
    )

  
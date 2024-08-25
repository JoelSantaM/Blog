from django import forms
from .models import Producto, Usuario

class ProductoModelForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'cuerpo']
    
class UsuarioModelForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'email']

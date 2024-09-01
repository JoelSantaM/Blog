from django import forms
from .models import Producto
from django.core.exceptions import ValidationError
from django.utils import timezone


class ProductoModelForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['titulo', 'contenido', 'fecha_publicacion', 'categoria', 'autor']
    
    fecha_publicacion = forms.DateField(
        input_formats=['%d/%m/%Y'],
        widget=forms.DateInput(format='%d/%m/%Y')
    )

    def clean_titulo(self):
        titulo = self.cleaned_data.get('titulo')
        if not titulo:
            raise ValidationError("Porfavor, agrega un titulo")
        return titulo
    
    def clean_fecha_publicacion(self):
        fecha_publicacion = self.cleaned_data.get('fecha_publicacion')
        if fecha_publicacion and fecha_publicacion > timezone.now().date():
            raise ValidationError("La fecha de publicacion esta en futuro")
        return fecha_publicacion
from django import forms
from .models import Estudiante, Curso, Inscripcion
from django.core.validators import RegexValidator

class EstudianteForm(forms.ModelForm):
    telefono = forms.CharField(validators=[RegexValidator(r'^\+?1?\d{9,15}$', message="Número de teléfono inválido.")])

    class Meta:
        model = Estudiante
        fields = ['nombre', 'apellido', 'rut', 'email', 'direccion', 'telefono']

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields =  ['nombre', 'descripcion', 'tipo', 'vacantes', 'precio']

class InscripcionForm(forms.ModelForm):
    class Meta:
        model = Inscripcion
        fields = ['estudiante', 'curso', 'estado'] 

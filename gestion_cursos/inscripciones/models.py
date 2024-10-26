from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    rut = models.CharField(max_length=12)
    email = models.EmailField()
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Curso(models.Model):
    TIPO_CURSO = [('Obligatorio', 'Materia obligatoria'), ('Electivo', 'Materia electiva')]
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20, choices=TIPO_CURSO)
    descripcion = models.TextField()
    vacantes = models.PositiveIntegerField(validators=[MinValueValidator(0)])
    precio = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.0)])

class Inscripcion(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=[('Inscrito', 'Inscrito'), ('Cancelado', 'Cancelado'), ('Espera', 'En espera')])

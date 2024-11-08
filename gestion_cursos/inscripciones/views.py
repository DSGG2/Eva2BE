from django.shortcuts import render, get_object_or_404, redirect
from .models import Estudiante, Curso, Inscripcion
from .forms import EstudianteForm, CursoForm, InscripcionForm

def home(request):
    return render(request, 'inscripciones/home.html')

def inscripcion_list(request):
    inscripciones = Inscripcion.objects.all()
    return render(request, 'inscripciones/inscripcion_list.html', {'inscripciones': inscripciones})

def inscripcion_create(request):
    if request.method == 'POST':
        form = InscripcionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inscripcion_list')
    else:
        form = InscripcionForm()
    return render(request, 'inscripciones/inscripcion_form.html', {'form': form})

def inscripcion_update(request, id):
    inscripcion = get_object_or_404(Inscripcion, id=id)
    if request.method == 'POST':
        form = InscripcionForm(request.POST, instance=inscripcion)
        if form.is_valid():
            form.save()
            return redirect('inscripcion_list')
    else:
        form = InscripcionForm(instance=inscripcion)
    return render(request, 'inscripciones/inscripcion_form.html', {'form': form, 'inscripcion': inscripcion})

def inscripcion_delete(request, id):
    inscripcion = get_object_or_404(Inscripcion, id=id)
    if request.method == 'POST':
        inscripcion.delete()
        return redirect('inscripcion_list')
    return render(request, 'inscripciones/inscripcion_confirm_delete.html', {'inscripcion': inscripcion})

def curso_list(request):
    cursos = Curso.objects.all()
    return render(request, 'inscripciones/curso_list.html', {'cursos': cursos})

def curso_create(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('curso_list')
    else:
        form = CursoForm()
    return render(request, 'inscripciones/curso_form.html', {'form': form})

def curso_update(request, id):
    curso = get_object_or_404(Curso, id=id)
    if request.method == 'POST':
        form = CursoForm(request.POST, instance=curso)
        if form.is_valid():
            form.save()
            return redirect('curso_list')
    else:
        form = CursoForm(instance=curso)
    return render(request, 'inscripciones/curso_form.html', {'form': form, 'curso': curso})

def curso_delete(request, id):
    curso = get_object_or_404(Curso, id=id)
    if request.method == 'POST':
        curso.delete()
        return redirect('curso_list')
    return render(request, 'inscripciones/curso_confirm_delete.html', {'curso': curso})

def estudiante_list(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'inscripciones/estudiante_list.html', {'estudiantes': estudiantes})

def estudiante_create(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('estudiante_list')  # Redirige a la lista de estudiantes
    else:
        form = EstudianteForm()
    return render(request, 'inscripciones/estudiante_form.html', {'form': form})

def estudiante_update(request, id):
    estudiante = get_object_or_404(Estudiante, id=id)
    form = EstudianteForm(request.POST or None, instance=estudiante)
    if form.is_valid():
        form.save()
        return redirect('estudiante_list')
    return render(request, 'inscripciones/estudiante_form.html', {'form': form})

def estudiante_delete(request, id):
    estudiante = get_object_or_404(Estudiante, id=id)
    if request.method == 'POST':
        estudiante.delete()
        return redirect('estudiante_list')
    return render(request, 'inscripciones/estudiante_confirm_delete.html', {'estudiante': estudiante})

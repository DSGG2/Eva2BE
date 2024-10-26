from django.urls import path
from . import views

urlpatterns = [
     path('', views.home, name='home'),
    path('estudiantes/', views.estudiante_list, name='estudiante_list'),
    path('estudiantes/nuevo/', views.estudiante_create, name='estudiante_create'),
    path('estudiantes/<int:id>/editar/', views.estudiante_update, name='estudiante_update'),
    path('estudiantes/<int:id>/eliminar/', views.estudiante_delete, name='estudiante_delete'),  
    path('cursos/', views.curso_list, name='curso_list'),
    path('cursos/nuevo/', views.curso_create, name='curso_create'),
    path('cursos/<int:pk>/editar/', views.curso_update, name='curso_update'),
    path('cursos/<int:pk>/eliminar/', views.curso_delete, name='curso_delete'),
    path('inscripciones/', views.inscripcion_list, name='inscripcion_list'),
    path('inscripciones/nuevo/', views.inscripcion_create, name='inscripcion_create'),
    path('inscripciones/<int:id>/editar/', views.inscripcion_update, name='inscripcion_update'),
    path('inscripciones/<int:id>/eliminar/', views.inscripcion_delete, name='inscripcion_delete'),
]

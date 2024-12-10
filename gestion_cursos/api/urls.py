from django.urls import path, include
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.routers import DefaultRouter
from .views import CursoViewSet, EstudianteViewSet, InscripcionViewSet

router = DefaultRouter()
router.register('cursos', CursoViewSet, basename='curso')
router.register('estudiantes', EstudianteViewSet, basename='estudiante')
router.register('inscripciones', InscripcionViewSet, basename='inscripcion')

@api_view(['GET'])
def api_root(request):
    return Response({
        'cursos': '/api/cursos/',
        'estudiantes': '/api/estudiantes/',
        'inscripciones': '/api/inscripciones/',
    })

urlpatterns = [
    path('', api_root), 
] + router.urls

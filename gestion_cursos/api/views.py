from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from inscripciones.models import Curso,Estudiante,Inscripcion
from .serializers import CursoSerializer,EstudianteSerializer,InscripcionSerializer

class InscripcionViewSet(ModelViewSet):
    queryset = Inscripcion.objects.all()
    serializer_class = InscripcionSerializer

class InscripcionList(APIView):
    def get(self, request):
        inscripciones = Inscripcion.objects.all()
        serializer = InscripcionSerializer(inscripciones, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = InscripcionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class InscripcionDetail(APIView):
    def get_object(self, pk):
        try:
            return Inscripcion.objects.get(pk=pk)
        except Inscripcion.DoesNotExist:
            return None

    def get(self, request, pk):
        inscripcion = self.get_object(pk)
        if inscripcion is None:
            return Response({'error': 'Inscripción no encontrada'}, status=status.HTTP_404_NOT_FOUND)
        serializer = InscripcionSerializer(inscripcion)
        return Response(serializer.data)

    def put(self, request, pk):
        inscripcion = self.get_object(pk)
        if inscripcion is None:
            return Response({'error': 'Inscripción no encontrada'}, status=status.HTTP_404_NOT_FOUND)
        serializer = InscripcionSerializer(inscripcion, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        inscripcion = self.get_object(pk)
        if inscripcion is None:
            return Response({'error': 'Inscripción no encontrada'}, status=status.HTTP_404_NOT_FOUND)
        inscripcion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class EstudianteViewSet(ModelViewSet):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer

class EstudianteList(APIView):
    def get(self, request):
        estudiantes = Estudiante.objects.all()
        serializer = EstudianteSerializer(estudiantes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EstudianteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EstudianteDetail(APIView):
    def get_object(self, pk):
        try:
            return Estudiante.objects.get(pk=pk)
        except Estudiante.DoesNotExist:
            return None

    def get(self, request, pk):
        estudiante = self.get_object(pk)
        if estudiante is None:
            return Response({'error': 'Estudiante no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        serializer = EstudianteSerializer(estudiante)
        return Response(serializer.data)

    def put(self, request, pk):
        estudiante = self.get_object(pk)
        if estudiante is None:
            return Response({'error': 'Estudiante no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        serializer = EstudianteSerializer(estudiante, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        estudiante = self.get_object(pk)
        if estudiante is None:
            return Response({'error': 'Estudiante no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        estudiante.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CursoViewSet(ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    
class CursoList(APIView):
    def get(self, request):
        cursos = Curso.objects.all()
        serializer = CursoSerializer(cursos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CursoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CursoDetail(APIView):
    def get_object(self, pk):
        try:
            return Curso.objects.get(pk=pk)
        except Curso.DoesNotExist:
            return None

    def get(self, request, pk):
        curso = self.get_object(pk)
        if curso is None:
            return Response({'error': 'Curso no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        serializer = CursoSerializer(curso)
        return Response(serializer.data)

    def put(self, request, pk):
        curso = self.get_object(pk)
        if curso is None:
            return Response({'error': 'Curso no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        serializer = CursoSerializer(curso, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        curso = self.get_object(pk)
        if curso is None:
            return Response({'error': 'Curso no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        curso.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


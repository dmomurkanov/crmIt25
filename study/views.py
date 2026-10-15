from rest_framework import viewsets
from .models import *
from .serializers import *

class FacultyViewSet(viewsets.ModelViewSet):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer


class DirectionViewSet(viewsets.ModelViewSet):
    queryset = Direction.objects.all()
    serializer_class = DirectionSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class DirectionManagerViewSet(viewsets.ModelViewSet):
    queryset = DirectionManager.objects.all()
    serializer_class = DirectionManagerSerializer


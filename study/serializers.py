from rest_framework import serializers
from .models import *


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = '__all__'


class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = '__all__'


class DirectionSerializer(serializers.ModelSerializer):
    faculty = FacultySerializer(read_only=True)

    class Meta:
        model = Direction
        fields = '__all__'


class DirectionManagerSerializer(serializers.ModelSerializer):
    direction = DirectionSerializer(read_only=True)

    class Meta:
        model = DirectionManager
        fields = '__all__'
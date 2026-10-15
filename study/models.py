from django.db import models


class Faculty(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Direction(models.Model):
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class DirectionManager(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    direction = models.OneToOneField(Direction, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=100)
    direction = models.ManyToManyField(Direction)

    def __str__(self):
        return self.name


def hello():
    return "hello"
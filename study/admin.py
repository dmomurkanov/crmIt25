from django.contrib import admin
from study.models import Faculty, Direction, DirectionManager, Student


@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    pass


@admin.register(Direction)
class FacultyAdmin(admin.ModelAdmin):
    pass


@admin.register(DirectionManager)
class DirectionManagerAdmin(admin.ModelAdmin):
    pass

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    pass
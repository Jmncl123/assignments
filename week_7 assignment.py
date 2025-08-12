from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Initial in-memory data
students = [
    {"id": 1, "name": "John Doe", "level": "100", "course": "Computer Science"},
    {"id": 2, "name": "Aisha Bello", "level": "200", "course": "Information Technology"},
    {"id": 3, "name": "Emeka Obi", "level": "300", "course": "Software Engineering"}
]

# Get all students
def get_students(request):
    return JsonResponse(students, safe=False)

# Create a new student
@csrf_exempt
def create_student(request):
    if request.method == "POST":
        data = json.loads(request.body)
        new_id = max(s["id"] for s in students) + 1
        data["id"] = new_id
        students.append(data)
        return JsonResponse({"message": "Student added successfully", "student": data}, status=201)

# Update a student
@csrf_exempt
def update_student(request, student_id):
    if request.method == "PUT":
        data = json.loads(request.body)
        for student in students:
            if student["id"] == student_id:
                student.update(data)
                return JsonResponse({"message": "Student updated successfully", "student": student})
        return JsonResponse({"error": "Student not found"}, status=404)

# Delete a student
@csrf_exempt
def delete_student(request, student_id):
    if request.method == "DELETE":
        global students
        students = [s for s in students if s["id"] != student_id]
        return JsonResponse({"message": "Student deleted successfully"})
student_project/urls.py
from django.contrib import admin
from django.urls import path
from student_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', views.get_students),
    path('students/add/', views.create_student),
    path('students/update/<int:student_id>/', views.update_student),
    path('students/delete/<int:student_id>/', views.delete_student),
]
Test with cURL or Postman
Get Students
curl http://127.0.0.1:8000/students/
Add Student
curl -X POST http://127.0.0.1:8000/students/add/ \
-H "Content-Type: application/json" \
-d '{"name": "Tosin Ade", "level": "100", "course": "Cybersecurity"}'
Update Student
curl -X PUT http://127.0.0.1:8000/students/update/1/ \
-H "Content-Type: application/json" \
-d '{"name": "John Doe Jr.", "level": "200"}'
Delete Student
curl -X DELETE http://127.0.0.1:8000/students/delete/1/
Part 2 — With Django Models & ORM
Once you get the in-memory version working, switch to the database.
Create a model in student_app/models.py:
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    level = models.CharField(max_length=10)
    course = models.CharField(max_length=100)

    def __str__(self):
        return self.name
Run migrations:
python manage.py makemigrations
python manage.py migrate
Replace the in-memory code with Django ORM queries in views.py:
from .models import Student

def get_students(request):
    students = list(Student.objects.values())
    return JsonResponse(students, safe=False)

@csrf_exempt
def create_student(request):
    if request.method == "POST":
        data = json.loads(request.body)
        student = Student.objects.create(**data)
        return JsonResponse({"message": "Student added", "id": student.id}, status=201)

@csrf_exempt
def update_student(request, student_id):
    if request.method == "PUT":
        data = json.loads(request.body)
        try:
            student = Student.objects.get(id=student_id)
            for key, value in data.items():
                setattr(student, key, value)
            student.save()
            return JsonResponse({"message": "Student updated"})
        except Student.DoesNotExist:
            return JsonResponse({"error": "Student not found"}, status=404)

@csrf_exempt
def delete_student(request, student_id):
    if request.method == "DELETE":
        try:
            student = Student.objects.get(id=student_id)
            student.delete()
            return JsonResponse({"message": "Student deleted"})
        except Student.DoesNotExist:
            return JsonResponse({"error": "Student not found"}, status=404)
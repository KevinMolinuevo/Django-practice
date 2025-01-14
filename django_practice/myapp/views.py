from django.shortcuts import render
from django.http import HttpResponse
from .models import Students, Teachers

# Create your views here.
def students_list(request):
    student_list = Students.objects.all()
    teacher_list = Teachers.objects.all()
    
    context = {
        'student_list': student_list,
        'teacher_list': teacher_list,
    }
    return render(request, 'student_teachers.html', context)
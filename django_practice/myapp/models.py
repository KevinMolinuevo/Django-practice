from django.db import models

# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length= 255)
    age = models.IntegerField()
    enrolled_date = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.name

def get_students_older_than_18():
    students = Students.objects.filter(age__gt=18)
    return [student.name for student in students]

class Teachers(models.Model):
    name =  models.CharField(max_length= 255)
    subject = models.CharField(max_length= 255)
    
    def __str__(self):
        return self.name
    
def get_students_younger_than_18():
    younger = Students.objects.filter(age__lt=18)
    return [student.name for student in students]

def get_students_by_subject():
    Class_1 = students
    Class_2 = younger
    
    return Class_1, Class_2 
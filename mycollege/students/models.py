from django.db import models
from datetime import datetime
# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=30)
    code = models.IntegerField()

    def __str__(self):
        return self.name

 
class Student_Data(models.Model):
    name = models.CharField(max_length=40)
    rollno = models.IntegerField()
    class_division = models.CharField(max_length=30)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    phone = models.IntegerField()
    address = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=55)

    
    def __str__(self):
        return self.name


class LeaveApplication(models.Model):
    appied_date = models.DateTimeField(default=datetime.now, blank=True)
    reason = models.CharField(max_length=500)
    student = models.ForeignKey(Student_Data, on_delete=models.CASCADE)
    from_date = models.CharField(max_length=322)
    to_date = models.CharField(max_length=322)

    def __str__(self):
        return self.student.name



class StudentsFeedback(models.Model):
    complain = models.CharField(max_length=100000)
    student = models.ForeignKey(Student_Data,on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
    appied_date = models.DateTimeField(default=datetime.now, blank=True)
    
    def __str__(self):
        return self.student.name


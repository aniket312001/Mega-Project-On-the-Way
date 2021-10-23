from django.db import models
from students.models import Course
from datetime import datetime
 
# Create your models here.
class Staff_Data(models.Model):
    name = models.CharField(max_length=40)
    staff_id = models.IntegerField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    class_division = models.CharField(max_length=30)
    phone = models.IntegerField()
    address = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=55)

    
    def __str__(self):
        return self.name


class Staff_Notification(models.Model):
    notification = models.CharField(max_length=100000)
    staff = models.ForeignKey(Staff_Data, on_delete=models.DO_NOTHING)
    date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.staff.name


class BlockListStudent(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=254)
    
    def __str__(self):
        return self.name
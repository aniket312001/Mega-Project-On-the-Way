from django.contrib import admin
from .models import Student_Data, Course, LeaveApplication, StudentsFeedback
# Register your models here.
admin.site.register(Student_Data)
admin.site.register(Course)
admin.site.register(LeaveApplication)
admin.site.register(StudentsFeedback)


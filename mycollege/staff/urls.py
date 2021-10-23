from django.urls import path,include
from . import views

urlpatterns = [
    path('login/',views.staff_login,name='staff_login'),
    path('profile/<str:pk>/',views.myprofile,name='staff_profile'),
    path('my_students/<str:pk>/',views.mystudents,name='staff_student'),
    path('leaveNote/<str:pk>/',views.seeLeaveApplication,name='staff_student_leave'),
    path('StudentProfile/<str:pk>',views.showStudentProfile, name='mystudent_profile'),
    path('notication/<str:pk>',views.send_Notification, name='mynotification'),
    path('delete/<str:pk>',views.deleteStudent, name='delete_S'),

]

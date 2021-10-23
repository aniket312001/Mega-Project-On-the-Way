from django.urls import path,include
from . import views

urlpatterns = [
    path('login/',views.admins_login,name='admins_login'),
    path('profile/<str:pk>',views.admins_profile,name='admins_profile'),
    path('profile/<str:pk>/feedback',views.show_feedback,name='show_feedback'),
    path('profile/<str:pk>/staff',views.show_Teacher,name='show_teacher'),
    path('profile/<str:pk>/student',views.show_Student,name='show_student'),
    path('profile/<str:ad>/studentProfile/<str:pk>',views.myStudentProfile, name='mystudent_profile'),
    path('profile/<str:ad>/staffProfile/<str:pk>',views.myStaffProfile, name='mystaff_profile'),
    path('profile/<str:ad>/DeleteStudentProfile/<str:pk>',views.deleteStudents, name='delete_Student'),
    path('profile/<str:ad>/DeleteStaffProfile/<str:pk>',views.delete_Staff, name='delete_Staff'),
    path('profile/<str:pk>/SendNotification',views.admin_Notification,name='admin_Notifications')
]

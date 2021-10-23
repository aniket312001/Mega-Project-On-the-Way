from django.urls import path,include
from . import views

urlpatterns = [
    path('login/', views.student_login, name='student_login'),
    path('register/', views.student_register, name='student_register'),
    # path('show/<str:pk>/', views.show, name='student_show'),
    # path('logout/', views.student_logout, name='student_logout'),
    path('leave/<str:pk>',views.student_leave_application, name='student_leave'),
    path('profile/<str:pk>',views.profile, name='student_profile'),
    path('feedback/<str:pk>',views.student_Feedback,name='student_feedback')
]

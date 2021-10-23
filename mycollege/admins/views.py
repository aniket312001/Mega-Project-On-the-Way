from django.shortcuts import render, redirect
from .models import AdminData,AdminNotification
from students.models import StudentsFeedback,Student_Data,Course
from staff.models import Staff_Data, BlockListStudent
from django.contrib import messages

# Create your views here.
def admins_login(request):

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['pwd']

        admin = AdminData.objects.filter(email=email,password=password)[0]

        if admin:
            return render(request,'admins/admin_profile.html',{'admin':admin,'value':'admin'})
        else:
            return redirect('admins_login')

    return render(request,'admins/admins_login.html')

def admins_profile(request,pk):
    admin = AdminData.objects.filter(name=pk)[0]
    return render(request,'admins/admin_profile.html',{'admin':admin,'value':'admin'})


def show_feedback(request,pk):
    admin = AdminData.objects.filter(name=pk)[0]
    feed = StudentsFeedback.objects.all()
    return render(request,'admins/feedback.html',{'feed':feed,'admin':admin,'value':'admin'})


def show_Teacher(request,pk):
    admin = AdminData.objects.filter(name=pk)[0]
    staff = Staff_Data.objects.all()
    course = Course.objects.all()
    return render(request,'admins/mystaff.html',{'staff':staff,'course':course,'admin':admin,'value':'admin'})


def show_Student(request,pk):
    admin = AdminData.objects.filter(name=pk)[0]
    stud = Student_Data.objects.all()
    course = Course.objects.all()
    return render(request,'admins/mystudent.html',{'student':stud,'course':course,'admin':admin,'value':'admin'})


def myStudentProfile(request,pk,ad):
    s1 = Student_Data.objects.filter(name=pk)[0]
    admin = AdminData.objects.filter(name=ad)[0]
    return render(request, 'students/dashboard.html',{'student':s1,'value':'admin','admin':admin})
    


def myStaffProfile(request,pk,ad):
    s1 = Staff_Data.objects.filter(name=pk)[0]
    admin = AdminData.objects.filter(name=ad)[0]
    return render(request, 'staff/teacher_profile.html',{'staff':s1,'value':'admin','admin':admin})
    

def deleteStudents(request,pk,ad):
    s1 = Student_Data.objects.filter(name=pk)[0]
    admin = AdminData.objects.filter(name=ad)[0]

    if request.method == 'POST':
        bls = BlockListStudent.objects.create(name=s1.name,email=s1.email) 
        bls.save()
        s1.delete()
        messages.info(request,"User has been deleted!")
        return render(request,'admins/admin_profile.html',{'admin':admin,'value':'admin'}) 

    return render(request,'staff/Delete_Student.html',{'student':s1,'value':'admin','admin':admin}) 


def delete_Staff(request,pk,ad):
    s1 = Staff_Data.objects.filter(name=pk)[0]
    admin = AdminData.objects.filter(name=ad)[0]

    if request.method == 'POST':
        bls = BlockListStudent.objects.create(name=s1.name,email=s1.email) 
        bls.save()
        s1.delete()
        messages.info(request,"User has been deleted!")
        return render(request,'admins/admin_profile.html',{'admin':admin,'value':'admin'}) 

    return render(request,'staff/Delete_Student.html',{'student':s1,'value':'admin','admin':admin})



def admin_Notification(request,pk):
    
    admin = AdminData.objects.filter(name=pk)[0]
    
    if request.method == 'POST':

        msg = request.POST['notf']
        # print(msg)

        note = AdminNotification.objects.create(notification=msg,admin=admin)
        note.save()
        messages.info(request,f"hello {note}, Your Notification will display to everyone")


    return render(request,'staff/notification.html',{'admin':admin,'value':'admin'})
    
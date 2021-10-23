from django.shortcuts import render,redirect
from .models import Staff_Data, Staff_Notification, BlockListStudent
from students.models import Student_Data,LeaveApplication
from django.contrib import messages
# Create your views here.
def staff_login(request):

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['pwd']
        # print(email,password)

        staff = Staff_Data.objects.filter(email=email,password=password)
        if staff:
            return render(request, 'staff/teacher_profile.html',{'staff':staff[0],"value":"staff"})  # value is for navbar 
        else:
            messages.info(request,"Invalid User")
            return redirect('staff_login')
        

    return render(request,'staff/staff_login.html')


def myprofile(request,pk):
    staff = Staff_Data.objects.filter(name=pk)
    return render(request, 'staff/teacher_profile.html',{'staff':staff[0],"value":"staff"})
    

def mystudents(request,pk):
    staff = Staff_Data.objects.filter(name=pk)[0]
    students = Student_Data.objects.filter(course=staff.course,class_division=staff.class_division)
    
    return render(request,'staff/my_students.html',{'student':students,'staff':staff,'value':'staff'})


def send_Notification(request,pk):
    
    staff = Staff_Data.objects.filter(name=pk)[0]
    
    if request.method == 'POST':

        msg = request.POST['notf']
        # print(msg)

        note = Staff_Notification.objects.create(notification=msg,staff=staff)
        note.save()
        messages.info(request,f"hello {note}, Your Notification will display to everyone")


    return render(request,'staff/notification.html',{'staff':staff,'value':'staff'})
    


def seeLeaveApplication(request,pk):
    staff = Staff_Data.objects.filter(name=pk)[0]
    students = Student_Data.objects.filter(course=staff.course,class_division=staff.class_division)
    
    leave = []
    for i in students:
        
        if (LeaveApplication.objects.filter(student=i)):
            leave.append(LeaveApplication.objects.filter(student=i))
    new = []    
    
    for i in leave:
        for j in i:
            new.append(j)  # in j we have all name of row inside the table
    
    lens = len(new)
  
  
    # bubble sort
    for i in range(lens-1):
        for j in range(0, lens-i-1):
            if new[j].appied_date < new[j + 1].appied_date :  # according to the date
                new[j], new[j + 1] = new[j + 1], new[j]

    
    return render(request, 'staff/student_leave_note.html',{'student':students,'staff':staff,'value':'staff','leave':new,'len':len(new)})



def showStudentProfile(request,pk):
    s1 = Student_Data.objects.filter(name=pk)[0]
    staff = Staff_Data.objects.filter(class_division=s1.class_division,course=s1.course)
    return render(request, 'students/dashboard.html',{'student':s1,'value':'staff','staff':staff[0].name})


def deleteStudent(request,pk):
    s1 = Student_Data.objects.filter(name=pk)[0]
    staff = Staff_Data.objects.filter(class_division=s1.class_division,course=s1.course)

    if request.method == 'POST':
        bls = BlockListStudent.objects.create(name=s1.name,email=s1.email) 
        bls.save()
        s1.delete()
        messages.info(request,"User has been deleted!")
        return render(request, 'staff/teacher_profile.html',{'staff':staff[0],"value":"staff"})

    return render(request,'staff/Delete_Student.html',{'student':s1,'value':'staff','staff':staff[0].name}) 
    
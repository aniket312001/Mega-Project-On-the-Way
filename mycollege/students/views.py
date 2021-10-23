from django.shortcuts import render,redirect
from .models import Student_Data,Course, LeaveApplication, StudentsFeedback
from django.contrib import messages
from staff.models import Staff_Data,BlockListStudent
from django.contrib.auth.models import User
# Create your views here.



def student_register(request):

    student = Student_Data.objects.all()
    my_Course = Course.objects.all()
    my_class = ['FY','SY','TY']

    if request.method == 'POST':

        name = request.POST['name']
        rollno = request.POST['rollno']
        new_class = request.POST['myclass']
        course = request.POST['course']
        phone = request.POST['phone']
        address = request.POST['addr']
        email = request.POST['email']
        password = request.POST['pwd']
        password2 = request.POST['pwd2']
        print(course)
        if BlockListStudent.objects.filter(email=email).exists():
            messages.info(request,"You have been blocked so kindly contact to your respected class teacher")
        else:
            if password == password2:
                if Student_Data.objects.filter(email=email).exists():
                    messages.info(request,"Email is Already Exist")
                    return redirect('student_register')

                elif Student_Data.objects.filter(rollno = rollno).exists():
                    messages.info(request,"Rollno is already taken kindly connect to Teacher/HOD")
                    return redirect('student_register')
                
                else:
                    # IMP
                    c1 = Course.objects.filter(name=course)   #Output --->  <QuerySet [<Course: BA>]>
                    print(c1)
                    for i in c1:  # we have to take value inside of queryset so use for-loop
                        student = Student_Data.objects.create(name=name,rollno=rollno,class_division=new_class,course=i,phone=phone,address=address,email=email,password=password)
                        student.save()
                        
                        # i user this to put authentication on a table
                        # user = User.objects.create_user(username=name, email=email, password=password)
                        # user.save()  # 

                        messages.info(request,f"Thanks for Signin {name}")
                    return redirect('student_login')
            else:
                messages.info(request,"Passord 1 should be match to password 2")
                return redirect('student_register')
        

    return render(request, 'students/student_register.html',{'course':my_Course,'class':my_class})


def student_login(request):

    if request.method == 'POST':
        
        email = request.POST['email']
        password = request.POST['pwd']
        # user = auth.authenticate(username=username, password=password)
        student = Student_Data.objects.filter(email=email,password=password)  # if student data is present 
        staff = Staff_Data.objects.all()  # teacher
        
        if student:
            return render(request, 'students/dashboard.html',{'student':student[0],'staff':staff,'value':'student'})
        else:
            messages.info(request,"Invalid User")
            return redirect('student_login')
            

    return render(request, 'students/student_login.html')





def profile(request,pk):
    s1 = Student_Data.objects.filter(name=pk)
    return render(request, 'students/dashboard.html',{'student':s1[0],'value':'student'})
    






def student_leave_application(request,pk):
    # print(pk)

    if request.method == 'POST':
        reason = request.POST['re']
        from_date = request.POST['from']
        to_date = request.POST['to']

        s1 = Student_Data.objects.filter(name=pk)

        for i in s1:
            leave_app =  LeaveApplication.objects.create(reason=reason,from_date=from_date,to_date=to_date,student=i)
            leave_app.save()
        
        
        messages.info(request,f"hello {s1[0]}, Your Leave Note has been send to your Respected Class Teacher")
    else :
        s1 = Student_Data.objects.filter(name=pk)  # in else because what if we not submit the form it will not run if block so  
    return render(request,'students/leave.html',{'student':s1[0],'value':'student'})


def student_Feedback(request,pk):
    s1 = Student_Data.objects.filter(name=pk)
    if request.method == 'POST':

        complain = request.POST['comp']

        for i in s1:
            s_f = StudentsFeedback.objects.create(complain=complain,student=i,course=i.course)
            s_f.save()
            messages.info(request,f"hello {s_f}, Thankyou for Your Feedback we will contact you as soon as possible")

    return render(request,'students/feedback.html',{'student':s1[0],'value':'student'})
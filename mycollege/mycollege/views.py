from django.http import HttpResponse
from django.shortcuts import render
from staff.models import Staff_Notification
from admins.models import AdminNotification

def home(request):
    staffnote = Staff_Notification.objects.all()
    adminnote = AdminNotification.objects.all()
    lst = []

    for i in staffnote:
        lst.append(i)
    
    for i in adminnote:
        lst.append(i)
    
    lens = len(lst)
  
  
    # bubble sort
    for i in range(lens-1):
        for j in range(0, lens-i-1):
            if lst[j].date < lst[j + 1].date :  # according to the date
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

    return render(request,'home.html',{'lst':lst})


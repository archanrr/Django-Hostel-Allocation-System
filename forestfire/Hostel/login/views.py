from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader
from login.models import Register,hostel,rooms,Students
from django.db.models import Q

def register_page(request):
    return render(request, 'College/hostel_admin.html')

def signin(request):
    if request.method=='POST':
        user=request.POST['username_login']
        password=request.POST['password_login']
        p =Register(username_login=user, password_login=password)
        p.save()
    return HttpResponse("Student Sucessfullly Added to database ask him to login and generate romm and hostel")

def login_user(request):
    if request.method=='POST':
        user=request.POST['username']
        password=request.POST['password']
        try:
            dbcheck=Register.objects.get(username_login=user)
        except:
            return HttpResponse("Login Does not Exist")

        if dbcheck.password_login!=password:
            return HttpResponse("Login failed")
        try:
             dbpassword=Students.objects.get(name=user)
        except:
             return render(request,'Register/StudentInfo.html')
        
        return render(request,'Register/Student.html',{ 'details':dbpassword })
        
    return HttpResponse("Login failed")

def hostelAllocation(request):
    if request.method=='POST':
        name=request.POST['name']
        dept=request.POST['dept']
        year=request.POST['year']
        address=request.POST['address']
        phone=request.POST['phone']
        try:
            hid=hostel.objects.get(id=year)
        except:
            h=hostel(id=year,warden='Thygarangan',no_of_rooms=70)
            h.save()
            hid=hostel.objects.get(id=year)
        if(hid.id >0):
            try:
                roomid=rooms.objects.get(Q(hostelid=hid.id) & Q(dept=dept) & ~Q(no_of_students=0))
            except:
                roomid=rooms(hostelid=hid,no_of_students=3,dept=dept)
                roomid.save()

            search=rooms.objects.get(Q(id=roomid.id) & Q(dept=dept))
            if search.no_of_students>0:
                search.no_of_students-=1
                search.save()
                p=Students(roomid=search,name=name,dept=dept,year=year,address=address,phone=phone)
                p.save()
            else:
                try:
                    search=rooms.objects.get(Q(dept=dept) & ~Q(no_of_students=0))
                except:
                    roomid=rooms(hostelid=hid,no_of_students=2,dept=dept)
                    roomid.save()
                    #print(roomid.dept)
                p=Students(roomid=search,name=name,dept=dept,year=year,address=address,phone=phone)
                p.save()
        else:
            return HttpResponse("Insertion Failed")

    fulldb=Students.objects.order_by('dept')
    return render(request,'Register/allot.html',{ 'student':p , 'hostel':hid.id,'full':fulldb })
        

def StudentHostelAllocation(request):
    return render(request,'College/StudentHostelAllocation.html')

def Studentlogin(request):
    return render(request,'Register/login.html')   

def adminlogin(request):
    return render(request,'College/adminlogin.html')


    
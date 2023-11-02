from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from schoolapp.models import Department


# Create your views here.
def index(request):
    return HttpResponse("hello welcome to school store")

def index(request):
    department=Department.objects.all()
    context={
        'School_page':Department
    }
    return render(request,'index.html',context)

def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not  None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid credentials")
            return redirect('/')
    return render(request,"login.html")




def register(request):
    if request.method== 'POST':
        username=request.POST['username']
        # first_name = request.POST['first_name']
        # last_name = request.POST['last_name']
        # email= request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']

        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Taken")
                return redirect('register')
            # elif User.objects.filter(email=email).exists():
            #     messages.info(request, "email Taken")
            #     return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password)
                user.save();
                return redirect('login')
            print("user created")
        else:
            messages.info(request,"password not matched")
            return redirect('register')
        return redirect('/')
    return render(request, "register.html")




def form(request):
    if request.method == 'POST':
        Name = request.POST['Name']
        DOB = request.POST['DOB']
        Age = request.POST['Age']
        Gender = request.POST['Gender']
        PhoneNumber = request.POST['PhoneNumber']
        Address = request.POST['Address']
        # Department = request.POST['Department']
        # Courses = request.POST['Courses']
        # Purpose = request.POST['Purpose']
        # MaterialsProvided = request.POST['MaterialsProvided']

    return render(request, "form.html")

def logout(request):
    auth.logout(request)
    return redirect('/')



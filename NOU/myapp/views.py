from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login 
from django.contrib import messages
# for the using aauthenticate and login we have to import this
# Create your views here.
def home(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(username=username,
                          password=password)
        
        if user:
            login(request,user)
            messages.success(request,"login sucessfully")
            return redirect("superadmindesh")
            
    messages.error(request,"login failed")    
    return render(request,"login.html")
def superadmindesh(request):
    return render(request,"superadmin/deshboard.html")

def base(request):
    return render(request,"superadmin/base.html")

def students(request):
    return render(request, 'superadmin/students.html')


def teachers(request):
    return render(request, 'superadmin/teachers.html')

def add_session(request):
    return render(request,'add_session.html')
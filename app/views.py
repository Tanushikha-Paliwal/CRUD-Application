from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from django.http.response import HttpResponse
from .models import *

# Create your views here.


def index(request):
    return render(request, "index.html")


# User creation


def registration(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        password = make_password(request.POST["password"])
        if User.objects.filter(email=email).exists():
            return HttpResponse("Email already exists")
        else:
            User.objects.create(name=name, email=email, password=password)
            return redirect('/userlogin/')


def table(request):
    data = User.objects.all()
    return render(request, "table.html", {"data": data})


#  call User update
def update_view(request, uid):
    res = User.objects.get(id=uid)
    return render(request, "update.html", {"data": res})

# update usser
def Update_form_data(request):
    if request.method == "POST":
        uid = request.POST["uid"]
        name = request.POST["name"]
        email = request.POST["email"]
        User.objects.filter(id=uid).update(name=name, email=email)
        return redirect("/table/")

def Delete_form_data(request, pk):
        User.objects.filter(id=pk).delete()
        return redirect("/table/")
    

def Login(request):
    return render(request,"login.html")

def User_Login(request):
    if request.method == "POST":
        email = request.POST['email']
        user_password = request.POST['password']
        if User.objects.filter(email=email).exists():
            obj = User.objects.get(email=email)
            password = obj.password
            if check_password(user_password,password):
                return redirect("/table/")
            else:
                return HttpResponse("password incorrect")
    else:
        return HttpResponse("Email  is not registered")

    

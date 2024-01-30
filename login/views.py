from django.views import View
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages


class Index(View):
    def get(self, request):
        return render(request, "index.html")
    
    def post(self, request):
        uname = request.POST.get("username")
        print("Hello {}".format(uname))
        return redirect("index")

class Login(View): 
    def get(self, request):
        return render(request, "login.html")
    
class Register(View):
    def get(self, request):
        return render(request, "register.html")
    
    def post(self, request):
        uname = request.POST.get("username", "")
        passwd = request.POST.get("password", "")
        user = User.objects.filter(username=uname).first()
        if user is None:
            user = User(username=uname)
            user.set_password(passwd)
            user.save()
            login(request, user)
            messages.success(request, "User created")
            return redirect("index")
        else:
            messages.info(request, "User already exists")
            return redirect("register")


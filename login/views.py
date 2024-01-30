from django.views import View
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


class Index(View):
    def get(self, request):
        return render(request, "index.html")
    
    def post(self, request):
        uname = request.POST.get("username")
        print("Hello {}".format(uname))
        return redirect("index")

class Login(View): 
    def get(self, request):
        if request.user.is_authenticated:
            messages.info(request, "You are already logged in , kindly logout first!")
            return redirect("index")
        return render(request, "login.html")
    
    def post(self, request):
        uname = request.POST.get("username", "")
        passwd = request.POST.get("password", "")
        user = authenticate(username=uname, password=passwd)
        if user is not None:
            login(request, user)
            messages.success(request, "Logged in")
            return redirect("index")
        else:
            messages.warning(request, "Username or password is incorrect")
        return render(request, "login.html")


@method_decorator(login_required, name="dispatch")   
class Logout(View):
    def get(self, request):
        logout(request)
        messages.success(request, "Signed out!")
        return redirect("index")
    
class Register(View):
    def get(self, request):
        if request.user.is_authenticated:
            messages.info(request, "You are already logged in")
            return redirect("index")
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


from django.views import View
from django.http import HttpResponse
from django.shortcuts import redirect, render


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


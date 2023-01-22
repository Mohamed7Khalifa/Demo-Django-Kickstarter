from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate

# Create your views here.
@login_required(login_url='login')

def app(request):
    return render(request, 'user/index.html',{})

def loginPage(request):
    return render(request, 'user/login.html',{})

def register(request):
   if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        repassword=request.POST.get('re-password')

        if password!=repassword:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:
            my_user=User.objects.create_user(name,email,password)
            my_user.save()         
            print(name,email,password,repassword)
            return redirect('login.html')
   return render(request, 'user/register.html',{})


from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


from .form import CreateUserForm
# Create your views here.
#login_required(login_url='login')

def app(request):
    return render(request, 'user/index.html',{})

def loginPage(request):
    if request.method == 'POST':
        username =    request.POST.get('username')
        password =    request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect ("/home")
        else:
            messages.error(request,"Invalid  password.")

    context = {}
    return render(request, 'user/login.html',context)

def register(request):
   form = CreateUserForm()
   if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            userName=form.cleaned_data.get('username')
            messages.success(request,"Account has been Created Succefully Welcome "+userName)
            return redirect('/login')
        

   context = {'form':form}

   return render(request, 'user/register.html',context)


def LogUserOut(request):
    logout(request)
    return redirect('/login')


"""
def register(request):
   form = CreateUserForm()
   if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('login.html')

   context = {'form':form}

   return render(request, 'user/register.html',context)

   def register(request):
    SignedUser=CreateUserForm(request.POST)
    if SignedUser.is_valid():
         SignedUser.save()
         userName=SignedUser.cleaned_data.get('username')
         messages.success(request,"account has been created for"+userName)
         return redirect('login.html')
    SignedUser=CreateUserForm()
    return render(request,'user/register.html',{"form":SignedUser})
"""


 
